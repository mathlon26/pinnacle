import MetaTrader5 as this

class Get():
    def __init__(self, mt5_inst):
        self.mt5_inst = mt5_inst
    
    def market_data(self, symbol, timeframe, range=[0, 100]):
        try:
            if self.mt5_inst.started:
                print("success")
        except Exception as e:
                raise e
class Mt5():
    def __init__(self) -> None:
        self.get = Get(self)
        self.started = False
        
    def name(self):
        return self.__class__.__name__
    
    def start(self, callback_function=None, status_update=None):
        try:
            if callback_function:
                callback_function(" LOADING : Authorizing...")
            this.initialize()
            self.started = True
            status_update("started", True)
            if callback_function:
                callback_function("OK : Authorized succesfully")
        except Exception as e:
            if callback_function:
                callback_function(f"ERROR : {str(e)} Authorization failed. Check if you have the right loging details in your auth.yaml", 'RED')
            else:
                raise e
    
    def stop(self, callback_function=None, status_update=None):
        if self.started:
            try:
                if callback_function:
                    callback_function("LOADING: Shutting down...")
                this.initialize()
                self.started = False
                status_update("started", False)
                
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

