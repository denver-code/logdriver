class UnsecuredAPIEndpoints:
    def __init__(self, base_url):
        self.base_url = base_url
        self.unsecured_api = f"{self.base_url}/api/u"
        
        self.new_log =  f"{self.unsecured_api}/log"
        self.get = f"{self.unsecured_api}/log/{{reference}}"
        self.today = f"{self.unsecured_api}/logs"


class SecuredAPIEndpoints:
    def __init__(self, base_url):
        self.base_url = base_url
        self.secured_api = f"{self.base_url}/api/s"
        
        self.new_log =  f"{self.secured_api}/log"
        self.get = f"{self.secured_api}/log/{{reference}}"
        self.today = f"{self.secured_api}/logs"

        self.public_key = f"{self.base_url}/api/rsa/publicKey"
