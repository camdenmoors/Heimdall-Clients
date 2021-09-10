class API:
    host = ""
    port = 3000
    APIKey = ""

    def __init__(self, host, APIKey, port=3000, protocol="http"):
        self.host = host
        self.port = port
        self.protocol = protocol
        self.APIKey = APIKey