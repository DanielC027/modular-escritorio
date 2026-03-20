from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
import base64
import hashlib
import hmac


class AESCifrado:
    def __init__(self, iteraciones=200_000):
        self.iteraciones = iteraciones

    def _clave_derivada(self, contrasena: str, sal: bytes) -> bytes:
        return PBKDF2(
            contrasena.encode(), sal, dkLen=32, count=self.iteraciones  # AES-256
        )

    def encriptar(self, contrasena: str, texto_plano: str) -> dict:
        sal = get_random_bytes(16)
        clave = self._clave_derivada(contrasena, sal)

        cifrador = AES.new(clave, AES.MODE_GCM)
        texto_cifrado, tag = cifrador.encrypt_and_digest(texto_plano.encode())

        return {
            "sal": base64.b64encode(sal).decode(),
            "nonce": base64.b64encode(cifrador.nonce).decode(),
            "tag": base64.b64encode(tag).decode(),
            "texto": base64.b64encode(texto_cifrado).decode(),
        }

    def desencriptar(self, contrasena: str, datos: dict) -> str:
        sal = base64.b64decode(datos["sal"])
        nonce = base64.b64decode(datos["nonce"])
        tag = base64.b64decode(datos["tag"])
        texto = base64.b64decode(datos["texto"])

        clave = self._clave_derivada(contrasena, sal)

        cifrador = AES.new(clave, AES.MODE_GCM, nonce=nonce)
        texto_plano = cifrador.decrypt_and_verify(texto, tag)

        return texto_plano.decode()

    def obtener_payload_aleatorio(self) -> str:
        return base64.b64encode(get_random_bytes(16)).decode()

    def generar_HMAC(self, contrasena, msj):
        return hmac.new(contrasena, msj.encode(), hashlib.sha256).digest()
