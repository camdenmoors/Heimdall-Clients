from requests.api import head
from classes.API import API
from requests_toolbelt.multipart.encoder import MultipartEncoder
import requests
import io

class HDFFile:
    filename = ""
    json = ""
    public = False

    def __init__(self, filename: str, data: str, api: API, public=False) -> None:
        self.filename = filename
        self.data = data
        self.api = api
        self.public = public
    
    def upload(self):
        mp_encoder = MultipartEncoder(
            fields = {
                "filename": self.filename,
                "public": str(self.public),
                "evaluationTags": "",
                "data": (self.filename, io.StringIO(self.data), 'text/plain')
            }
        )
        return requests.post(f"{self.api.protocol}://{self.api.host}:{self.api.port}/evaluations", data=mp_encoder, headers={'Content-Type': mp_encoder.content_type, 'Authorization': self.api.APIKey})