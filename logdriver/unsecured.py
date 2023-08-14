import requests

from logdriver.endpoints import UnsecuredAPIEndpoints
from logdriver.models import NewLogRequest


class UnsecuredDriver(object):
    def __init__(self, service_name: str, url: str = "http://localhost:8000"):
        self.unsecured_endpoints = UnsecuredAPIEndpoints(url)
        self.service_name = service_name


    def log(self, payload: dict, level: str = "INFO") -> str:
        """
        Send a log to the log server and return the reference id
        """
        r = requests.post(
            self.unsecured_endpoints.new_log,
            data=NewLogRequest(
                service=self.service_name,
                level=level,
                payload=payload
            ).model_dump_json(), 
            headers={"Content-Type": "application/json"}
        )
        if "reference" in r.json():
            return r.json()["reference"]

        return r.json()


    def get(self, reference: str) -> dict:
        """
        Get a log from the log server by its reference id
        """
        r = requests.get(
            self.unsecured_endpoints.get.format(reference=reference)
        )

        return r.json()
    

    def today(self, offset: int = 0, limit:int = 100, service = None, level = None) -> dict:
        """
        Get all logs from today
        """
        params = {"offset": offset, "limit": limit}
        if service:
            params["service"] = service
        if level:
            params["level"] = level

        r = requests.get(
            self.unsecured_endpoints.today,
            params=params
        )

        return r.json()
    

    def __repr__(self):
        return f"UnsecuredDriver(service_name={self.service_name}, url={self.unsecured_endpoints.base_url})"
    

    def __str__(self):
        return f"UnsecuredDriver(service_name={self.service_name}, url={self.unsecured_endpoints.base_url})"
