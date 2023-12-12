from .technicalAnalysis import technicalAnalysis as TA
from .mt5 import Mt5
from .logger import Logger
import json
import yaml
class Set():
    def __init__(self):
        pass
    
    def edit(self, key, value):
        try:
            with open("config.json", "r") as config_file:
                config = json.load(config_file)
        except FileNotFoundError:
            config = {}
            
        config[key] = value
        
        with open("config.json", "w") as config_file:
            json.dump(config, config_file, indent=2)
        
    def lot_size(self, size):
        self.edit("lotsize", size)
        
    def stop_loss(self, sl):
        self.edit("stoploss", sl)
        
    def take_profit(self, tp):
        self.edit("takeprofit", tp)
        
    def leverage(self, leverage):
        self.edit("leverage", leverage)
        
    def symbols_to_trade(self, symbols):
        self.edit("symbols_to_trade", symbols)
        
    def magic_number(self, magic_number):
        self.edit("magicnumber", magic_number)
        
    def max_orders(self, max_orders):
        self.edit("maxorders", max_orders)
        
    def risk_percentage(self, risk_percentage):
        self.edit("riskpercentage", risk_percentage)
        
    def trailing_stop(self, trailing_stop):
        self.edit("trailingstop", trailing_stop)
        
    def slippage(self, slippage):
        self.edit("slippage", slippage)
        
    def trade_comment(self, trade_comment):
        self.edit("tradecomment", trade_comment)
        
    def account_type(self, account_type):
        self.edit("accounttype", account_type)
        
    def parameters(self, params):
        self.edit("customindicatorparameters", params)
        
    def max_drawdown(self, max_dd):
        self.edit("maxdrawdown", max_dd)
        
class Get():
    def __init__(self):
        pass
    
    def get(self, key):
        try:
            with open("config.json", "r") as config_file:
                config = json.load(config_file)
        except FileNotFoundError:
            config = {}
            
        return config[key]
        
    def lot_size(self):
        return self.get("lotsize")
        
    def stop_loss(self):
        return self.get("stoploss")
        
    def take_profit(self):
        return self.get("takeprofit")
        
    def leverage(self):
        return self.get("leverage")
        
    def symbols_to_trade(self):
        return self.get("symbols_to_trade")
        
    def magic_number(self):
        return self.get("magicnumber")
        
    def max_orders(self):
        return self.get("maxorders")
        
    def risk_percentage(self):
        return self.get("riskpercentage")
        
    def trailing_stop(self):
        return self.get("trailingstop")
        
    def slippage(self):
        return self.get("slippage")
        
    def trade_comment(self):
        return self.get("tradecomment")
        
    def account_type(self):
        return self.get("accounttype")
        
    def parameters(self):
        return self.get("customindicatorparameters")
        
    def max_drawdown(self):
        return self.get("maxdrawdown")
    
    
        

class Pinnacle():
    def __init__(self, auth_file):
        self.logger = Logger()
        self.mt5 = Mt5()
        self.ta = TA()
        self.set = Set()
        self.get = Get()
        self.auth_file = auth_file
    
    def serve_status(self):
        return self.status
        
    
    def account_info(self):
        return self.mt5.get.info()
    
    def buy(self):
        return self.mt5.get.info()
      
    def sell(self):
        return self.mt5.get.info()
    
    def close_all(self):
        return self.mt5.get.info()
        
    def login(self):
        with open(self.auth_file, 'r') as file:
            auth = yaml.safe_load(file)
            login = auth['authentication']['login']
            server = auth['authentication']['server']
            password = auth['authentication']['password']
        self.mt5.login(login, server, password)
        
        
    def start(self, callback_function=None, status_update=None):
        self.mt5.start(callback_function=callback_function)
    
    def stop(self, callback_function=None, status_update=None):
        self.mt5.stop(callback_function=callback_function)
        
    def name(self):
        return self.__class__.__name__
    
    
    
