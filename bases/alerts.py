import logging as log
from includes.setup import *
from config import *

class Alerts:
    def __init__(self, VSTATS_API: str, connect_to_api: object, **kwargs) -> None:
        self.VSTATS_API = VSTATS_API
        self.connect_to_api = connect_to_api
        self.__dict__.update(kwargs)

    def send_to_vstats(self,status: dict,fn_show: dict, load: str,space:str,count:int) -> None:
        j = {
            "api_token": VSTATS_TOKEN,
            "status": status,
            "fn_show": fn_show,
            "load": load,
            "space":space,
            "hostname":self.hostname,
            "count":count
        }
        full, _, _ = self.connect_to_api("", self.VSTATS_API, "", j=j)
        log.info(full)
        

    def generic_error(self,e) -> None:
        j = {
            "api_token": VSTATS_TOKEN,
            "error": 'true',
            "hostname":self.hostname
        }
        
        full, _, _ = self.connect_to_api("", self.VSTATS_API, "", j=j)
        log.info(full)
