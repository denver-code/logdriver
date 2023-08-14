import base64
import json
import requests

from logdriver.endpoints import SecuredAPIEndpoints
from logdriver.models import NewEncLogRequest
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding



class SecuredDriver(object):
    def __init__(self, service_name: str, token: str = "", url: str = "http://localhost:8001"):
        self.secured_endpoints = SecuredAPIEndpoints(url)
        self.service_name = service_name
        self.token = token
        self.public_key = self.fetch_public_key()

    def fetch_public_key(self):
        """
        Fetch the public key from the log server
        """
        r = requests.get(self.secured_endpoints.public_key)
        key_data = r.content.replace(b'\\n', b'\n')
        key_data = key_data.replace(b'"', b'')
        publicKey = load_pem_public_key(key_data, backend=default_backend())

        return publicKey

    def log(self, payload: dict, level: str = "INFO") -> str:
        """
        Send a log to the log server and return the reference id
        """
        encrypted = base64.b64encode(self.public_key.encrypt(
            json.dumps(payload).encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        ))
        r = requests.post(
            self.secured_endpoints.new_log,
            data=NewEncLogRequest(
                level=level,
                payload=encrypted
            ).model_dump_json(), 
            headers={"Content-Type": "application/json",
                     "Authorisation": self.token}
        )
        if "reference" in r.json():
            return r.json()["reference"]

        return r.json()


    def get(self, reference: str, token: str = "") -> dict:
        """
        Get a log from the log server by its reference id
        """
        r = requests.get(
            self.secured_endpoints.get.format(reference=reference),
             headers={"Authorisation": self.token if token == "" else token}
        )

        return r.json()
    

    def today(self, offset: int = 0, limit:int = 100, service = None, level = None, token: str = "") -> dict:
        """
        Get all logs from today
        """
        params = {"offset": offset, "limit": limit}
        if service:
            params["service"] = service
        if level:
            params["level"] = level

        r = requests.get(
            self.secured_endpoints.today,
            params=params,
            headers={"Authorisation": self.token if token == "" else token}
        )

        return r.json()
    

    def __repr__(self):
        return f"UnsecuredDriver(service_name={self.service_name}, url={self.secured_endpoints.base_url})"
    

    def __str__(self):
        return f"UnsecuredDriver(service_name={self.service_name}, url={self.secured_endpoints.base_url})"
