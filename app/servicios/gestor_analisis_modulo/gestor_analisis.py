# from ...nucleo.analisis_modulo.analisis_ia_modulo import AnalisisANN

from ...nucleo.analisis_modulo.analisis_ia_modulo import AnalisisANN
from ..gestor_conexion_websocket.gestor_conexion_ws import BackendWSService
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
