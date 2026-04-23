import websockets
import json


class WSService:
    def __init__(self, url: str, auth_service):
        self.url = url
        self.auth_service = auth_service
        self.ws = None

    async def conectar(self):
        headers = {"Cookie": self.auth_service.get_cookie_header()}

        self.ws = await websockets.connect(self.url, additional_headers=headers)

    async def enviar(self, data: dict):
        if not self.ws:
            raise RuntimeError("WS no conectado")

        await self.ws.send(json.dumps(data))

    async def recibir(self):
        if not self.ws:
            raise RuntimeError("WebSocket no conectado")

        try:
            return await self.ws.recv()
        except websockets.exceptions.ConnectionClosed:
            print("Conexión cerrada")
            return None

    async def cerrar(self):
        if self.ws:
            await self.ws.close()
