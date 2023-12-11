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
    
    def start(self, callback_function=None):
        try:
            if callback_function:
                callback_function(" / : Authorizing...", 'BLUE')
            this.initialize()
            self.started = True
            if callback_function:
                callback_function("√ : Authorized succesfully", 'GREEN')
        except Exception as e:
            if callback_function:
                callback_function(f"Authorization failed. Error: {str(e)} \n Check if you have the right loging details in your auth.yaml", 'RED')
            else:
                raise e
    
    def stop(self, callback_function=None):
        if self.started:
            try:
                if callback_function:
                    callback_function(" / : Shutting down...", 'BLUE')
                this.initialize()
                self.started = False
                if callback_function:
                    callback_function("√ : Shut down succesfully", 'GREEN')
            except Exception as e:
                if callback_function:
                    callback_function(f"Shut down failed. Error: {str(e)} \n", 'RED')
                else:
                    raise e
        else:
            if callback_function:
                    callback_function(f"Error: Bot has not started yet. \n", 'RED')

