# from ...nucleo.analisis_modulo.analisis_ia_modulo import AnalisisANN

from ...nucleo.analisis_modulo.analisis_ia_modulo import AnalisisANN
from ..gestor_conexion_websocket.gestor_conexion_ws import BackendWSService

from ...bd.repositorios.escrito_repo import obtener_id_escrito
from ...bd.repositorios.analisis_repo import (
    crear_analisis_escrito,
    revisar_existe_analisis_en_bd,
    obtener_id_analisis,
    existe_emocion,
    existe_lista_emociones,
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

    def guardar_analisis(self, analisis):  # revisar si crea mas analisis
        # crear analisis escrito
        id_escrito = analisis["id_escrito"]
        existe_analisis = revisar_existe_analisis_en_bd(id_escrito)
        if not existe_analisis:
            crear_analisis_escrito(id_escrito)
        # obtener id_analisis
        id_analisis = obtener_id_analisis(id_escrito)
        # recorrer emociones
        #     emocion por emocionz
        for emocion in analisis["valores"]["etiquetas"]:
            # revisar si ya existe la emocion
            #     si: nada
            #     no: guardarla
            print(emocion)
            print(analisis["valores"]["probabilidades"])
            print(analisis["valores"]["etiquetas"])
            print(id_analisis)
            # revisar si existe lista emociones
            si_existe_emocion = existe_emocion(emocion)
            if si_existe_emocion:  #     si: registrar emocion en lista
                print("si exist emocion")
            else:  #     no: CREAR LISTA EMOCIONES CON ID_ANALISIS
                # existe lista emociones con id_analisis?
                si_existe_lista_emociones = existe_lista_emociones(id_analisis)

                if si_existe_lista_emociones:  #    si: actualizar lista
                    print("si existe lista emociones")
                else:  #    no: crear una
                    print("no existe lista emociones")
            #          registrar emocion en lista
            # regresar a: recorrer emociones
        print(analisis)
