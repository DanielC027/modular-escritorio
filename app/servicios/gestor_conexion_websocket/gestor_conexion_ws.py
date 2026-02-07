import asyncio
import json
import websockets


class BackendWSService:
    def __init__(self, url: str):
        self.url = url
        self.ws = None

    async def conectar(self):
        self.ws = await websockets.connect(self.url)

    async def enviar(self, data: dict):
        if not self.ws:
            raise RuntimeError("WebSocket no conectado")

        mensaje = json.dumps(data)
        await self.ws.send(mensaje)

    async def recibir(self):
        if not self.ws:
            raise RuntimeError("WebSocket no conectado")

        return await self.ws.recv()

    async def cerrar(self):
        if self.ws:
            await self.ws.close()
