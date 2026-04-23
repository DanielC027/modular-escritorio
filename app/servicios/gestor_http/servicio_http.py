import httpx


class HTTPService:
    def __init__(self, base_url: str, auth_service):
        self.base_url = base_url
        self.auth_service = auth_service

    async def guardar_analisis(self, data: dict):
        headers = {"Cookie": self.auth_service.get_cookie_header()}

        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/analisis/guardar_analisis", json=data, headers=headers
            )

            response.raise_for_status()
            return response.json()
