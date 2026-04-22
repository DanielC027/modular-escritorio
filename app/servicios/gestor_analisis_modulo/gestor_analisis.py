import asyncio
import threading
from collections import deque

from ...nucleo.analisis_modulo.analisis_ia_modulo import AnalisisANN
from ..gestor_conexion_websocket.gestor_conexion_ws import BackendWSService

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
        self.backend_ws = None
        self.ws_ready = False
        self.cola_mensajes = deque()

        self.loop = asyncio.new_event_loop()
        threading.Thread(target=self._run_loop, args=(self.loop,), daemon=True).start()

        asyncio.run_coroutine_threadsafe(self._conectar_ws(), self.loop)
        asyncio.run_coroutine_threadsafe(self._ws_worker(), self.loop)

    def _run_loop(self, loop):
        asyncio.set_event_loop(loop)
        loop.run_forever()

    async def _conectar_ws(self):
        try:
            ws = BackendWSService("ws://localhost:8000/ws")
            await ws.login()
            await ws.conectar()
            self.backend_ws = ws
            self.ws_ready = True
            print("Conectado al backend WebSocket")
        except Exception as e:
            self.backend_ws = None
            self.ws_ready = False
            print("Error al conectar WS:", e)

    async def _ws_worker(self):
        while True:
            if self.backend_ws and self.cola_mensajes:
                mensaje = self.cola_mensajes.popleft()
                try:
                    await self.backend_ws.enviar(mensaje)
                    print("Mensaje enviado desde worker")
                except Exception as e:
                    print("Error enviando WS:", e)
                    self.cola_mensajes.appendleft(mensaje)
            await asyncio.sleep(0.1)

    def analizar_texto(self, texto, progreso=None):
        analisis = AnalisisANN()
        return analisis.analizar_texto(texto)

    def enviar_datos_ws(self, mensaje):
        if not self.ws_ready or not self.backend_ws:
            self.cola_mensajes.append(mensaje)
            return

        async def enviar():
            try:
                await self.backend_ws.enviar(mensaje)
                print("Mensaje enviado al backend")
            except Exception as e:
                print("Error enviando WS:", e)

        asyncio.run_coroutine_threadsafe(enviar(), self.loop)

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

        except Exception as ex:
            print(ex)

    def obtener_analisis_dia(self, fecha, huella_digital):
        return obtener_datos_dia(fecha, huella_digital)

    def obtener_analisis_semana(self, fecha, huella_digital):
        return obtener_datos_semana(fecha, huella_digital)

    def obtener_analisis_mes(self, fecha, huella_digital):
        return obtener_datos_mes(fecha, huella_digital)

    def obtener_analisis_anio(self, fecha, huella_digital):
        return obtener_datos_anio(fecha, huella_digital)
