import asyncio
import threading

from collections import deque

from ...nucleo.analisis_modulo.analisis_ia_modulo import AnalisisANN
from ..gestor_conexion_websocket.gestor_conexion_ws import WSService
from ..gestor_auth.servicio_auth import AuthService
from ..gestor_http.servicio_http import HTTPService

from ...bd.repositorios.escrito_repo import obtener_id_escrito
from ...bd.repositorios.analisis_repo import (
    crear_analisis_escrito,
    revisar_existe_analisis_en_bd,
    obtener_id_analisis,
    obtener_id_emocion,
    obtener_datos_dia,
    obtener_datos_semana,
    obtener_datos_mes,
    obtener_datos_anio,
    existe_emocion,
    existe_emocion_en_analisis,
    crear_emocion,
    agregar_emocion_al_analisis,
    actualizar_emocion_del_analisis,
)


class GestorAnalisis:
    def __init__(self):
        self.loop = asyncio.new_event_loop()
        threading.Thread(target=self._run_loop, daemon=True).start()

        # Servicios
        self.auth = AuthService("http://localhost:8000")
        self.http = HTTPService("http://localhost:8000", self.auth)
        self.ws = WSService("ws://localhost:8000/ws", self.auth)

        # Estado
        self.ws_ready = False
        self.cola_ws = deque()

        # Init async
        asyncio.run_coroutine_threadsafe(self._init_services(), self.loop)
        asyncio.run_coroutine_threadsafe(self._ws_worker(), self.loop)

    def _run_loop(self):
        asyncio.set_event_loop(self.loop)
        self.loop.run_forever()

    async def _init_services(self):
        retry = 1

        while True:
            try:
                print("Login...")
                await self.auth.login("daniel@gmail.com", "America1?")

                print("Conectando WS...")
                await self.ws.conectar()

                self.ws_ready = True
                print("Todo listo 🚀")
                return

            except Exception as e:
                print("Error init:", e)
                await asyncio.sleep(retry)
                retry = min(retry * 2, 30)

    # ---------------- WS ----------------

    def enviar_ws(self, mensaje):
        self.cola_ws.append(mensaje)

    async def _ws_worker(self):
        while True:
            if self.ws_ready and self.cola_ws:
                msg = self.cola_ws.popleft()

                try:
                    await self.ws.enviar(msg)
                except Exception as e:
                    print("Error WS:", e)
                    self.ws_ready = False
                    self.cola_ws.appendleft(msg)

            await asyncio.sleep(0.1)

    # ---------------- HTTP ----------------

    def enviar_analisis_http(self, data):
        asyncio.run_coroutine_threadsafe(self.http.guardar_analisis(data), self.loop)

    # ANALISIS
    def analizar_texto(self, texto, progreso=None):
        analisis = AnalisisANN()
        return analisis.analizar_texto(texto)

    # GUARDADO EN BD (independiente del WS)
    def guardar_analisis(self, analisis):
        try:
            id_escrito = analisis["id_escrito"]

            if not revisar_existe_analisis_en_bd(id_escrito):
                crear_analisis_escrito(id_escrito)

            id_analisis = obtener_id_analisis(id_escrito)

            etiquetas = analisis["valores"]["etiquetas"]
            probabilidades = analisis["valores"]["probabilidades"]

            for i, emocion in enumerate(etiquetas):

                if not existe_emocion(emocion):
                    id_emocion = crear_emocion(emocion)
                else:
                    id_emocion = obtener_id_emocion(emocion)

                porcentaje = probabilidades[i]

                if existe_emocion_en_analisis(id_analisis, id_emocion):
                    actualizar_emocion_del_analisis(id_analisis, id_emocion, porcentaje)
                else:
                    agregar_emocion_al_analisis(id_analisis, id_emocion, porcentaje)
            print("Analisis a mandar a backend: ", analisis)
        except Exception as ex:
            print("Error guardando análisis:", ex)

    # CONSULTAS
    def obtener_analisis_dia(self, fecha, huella_digital):
        return obtener_datos_dia(fecha, huella_digital)

    def obtener_analisis_semana(self, fecha, huella_digital):
        return obtener_datos_semana(fecha, huella_digital)

    def obtener_analisis_mes(self, fecha, huella_digital):
        return obtener_datos_mes(fecha, huella_digital)

    def obtener_analisis_anio(self, fecha, huella_digital):
        return obtener_datos_anio(fecha, huella_digital)
