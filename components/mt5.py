import MetaTrader5 as this
from datetime import datetime, timedelta
import json
import yaml
   
class Mt5():
    def __init__(self) -> None:
        self.status = False
        self.id = None
        self.server_name = None
        self.password = None
        self.origin = this

        
    def name(self):
        return self.__class__.__name__
    
    def login(self, _login, _server, _password):
        this.initialize()
        self.id = _login
        self.server_name = _server
        self.password = _password
        this.login(login=_login, server=_server, password=_password)    
    
    def start(self, callback_function=None):
        if not self.status:
            try:
                if callback_function:
                    callback_function("LOADING : Authorizing...")
                this.initialize()
                self.status = True
                if callback_function:
                    callback_function("OK : Authorized succesfully")
            except Exception as e:
                if callback_function:
                    callback_function(f"ERROR : {str(e)} Authorization failed. Check if you have the right loging details in your auth.yaml", 'RED')
                else:
                    raise e
        else:
            if callback_function:
                    callback_function(f"ERROR : Bot already started. \n")
    def stop(self, callback_function=None):
        if self.status:
            try:
                if callback_function:
                    callback_function("LOADING: Shutting down...")
                this.initialize()
                self.status = False
                
                if callback_function:
                    callback_function("OK : Shut down succesfully")
            except Exception as e:
                if callback_function:
                    callback_function(f"ERROR : Shut down failed. Error: {str(e)} \n")
                else:
                    raise e
        else:
            if callback_function:
                    callback_function(f"ERROR : Bot has not started yet. \n")
                    
    def get_account_info(self):
        self.start()
        return this.account_info()
    
    def get_positions_total(self):
        self.start()
        return this.positions_total()
    
    
    def get_data(self):
        data = {}
        data["positions_total": self.get_positions_total()]
        
        return data
                    
        

