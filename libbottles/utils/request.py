import urllib.request, json 

from libbottles.utils import connection
from libbottles.exceptions import NoConnection

class Request:

    _headers = {}

    def __init__(self, headers: dict = None):
        self._headers["User-Agent"] = "libbottles client (usebottles.com)"

        if headers is not None:
            self._envs = {**self._headers, **headers}
        
        if not connection.check():
            raise NoConnection()
    
    def get(self, url: str):
        
        req = urllib.request.Request(
            url, 
            data=None, 
            headers=self._headers
        )

        with urllib.request.urlopen(req) as url:
            data = json.loads(url.read().decode())
            return data
