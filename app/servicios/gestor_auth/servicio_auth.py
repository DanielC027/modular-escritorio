import httpx


class AuthService:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.cookies = None

    async def login(self, email: str, password: str):
        url = f"{self.base_url}/auth/login"

        async with httpx.AsyncClient() as client:
            response = await client.post(
                url, json={"email": email, "password": password}
            )

            if response.status_code != 200:
                raise Exception(f"Error login: {response.status_code}")

            self.cookies = client.cookies

    def get_cookie_header(self):
        if not self.cookies:
            raise RuntimeError("No hay sesión")

        return "; ".join([f"{k}={v}" for k, v in self.cookies.items()])
