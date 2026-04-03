# from ...nucleo.analisis_modulo.analisis_ia_modulo import AnalisisANN

from ...nucleo.analisis_modulo.analisis_ia_modulo import AnalisisANN
from ..gestor_conexion_websocket.gestor_conexion_ws import BackendWSService

from ...bd.repositorios.escrito_repo import obtener_id_escrito
from ...bd.repositorios.analisis_repo import (
    crear_analisis_escrito,
    revisar_existe_analisis_en_bd,
    obtener_id_analisis,
)

import asyncio
import json
import threading


class GestorAnalisis:
    def __init__(self):
        # Crear loop de asyncio en un hilo separado
        self.loop = asyncio.new_event_loop()
        threading.Thread(target=self._run_loop, args=(self.loop,), daemon=True).start()

        # Inicializar WebSocket en el loop
        asyncio.run_coroutine_threadsafe(self._conectar_ws(), self.loop)

    def _run_loop(self, loop):
        asyncio.set_event_loop(loop)
        loop.run_forever()

    async def _conectar_ws(self):
        self.backend_ws = BackendWSService("ws://127.0.0.1:8000/ws")
        try:
            await self.backend_ws.conectar()
            print("Conectado al backend WebSocket")
        except Exception as e:
            print("Error al conectar WS:", e)

    def analizar_texto(self, texto, progreso=None):
        analisis = AnalisisANN()
        resultado = analisis.analizar_texto(texto)
        return resultado

    def enviar_datos_ws(self, mensaje):
        print("mensaje: ", mensaje)

        # Enviar al backend sin bloquear la UI
        async def enviar_ws():
            try:
                await self.backend_ws.enviar(mensaje)
                print("Mensaje enviado al backend")
            except Exception as e:
                print("Error enviando WS:", e)

        # Ejecutar en el loop del hilo
        asyncio.run_coroutine_threadsafe(enviar_ws(), self.loop)

    def guardar_analisis(self, analisis):
        # crear analisis escrito
        id_escrito = analisis["id_escrito"]
        existe_analisis = revisar_existe_analisis_en_bd(id_escrito)
        if not existe_analisis:
            print("crear analisis")

        # obtener id_analisis
        # recorrer emociones
        #     emocion por emocion
        # revisar si ya existe la emocion
        #     si: nada
        #     no: guardarla
        # revisar si existe lista emociones
        #     si: registrar emocion en lista
        #     no: CREAR LISTA EMOCIONES CON ID_ANALISIS
        #          registrar emocion en lista
        # regresar a: recorrer emociones
        print(analisis)
