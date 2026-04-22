import asyncio
import json
import websockets
import httpx


class BackendWSService:
    def __init__(self, url: str):
        self.url = url
        self.ws = None
        self.url_session = "http://localhost:8000/"
        self.cookie_header = None

    async def login(self):
        url_login = self.url_session + "auth/login"
        payload = {"email": "daniel@gmail.com", "password": "America1?"}

        async with httpx.AsyncClient() as client:
            response = await client.post(url_login, json=payload)

            if response.status_code != 200:
                raise Exception(f"Error en login: {response.status_code}")

            # Obtener cookies correctamente
            cookies = client.cookies
            self.cookie_header = "; ".join([f"{k}={v}" for k, v in cookies.items()])

            print("Cookies:", self.cookie_header)

    async def conectar(self):
        if not self.cookie_header:
            raise RuntimeError("Debes hacer login primero")

        try:
            headers = {"Cookie": self.cookie_header}

            self.ws = await websockets.connect(
                self.url, additional_headers=headers  # <- importante
            )

            print("WebSocket conexión creada")

        except Exception as ex:
            print("Error al crear conexión websocket:", ex)
            raise

    async def enviar(self, data: dict):
        if not self.ws:
            raise RuntimeError("WebSocket no conectado")

        mensaje = json.dumps(data)
        await self.ws.send(mensaje)

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
            print("WebSocket cerrado")
