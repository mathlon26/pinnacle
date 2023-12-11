from .technicalAnalysis import technicalAnalysis as TA
from .mt5 import Mt5
import json

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


class Status():
    def __init__(self, statusfile) -> None:
        self.path = statusfile
        self.status = open(statusfile, 'r')
        
    def set(self, key, value):
        try:
            with open(self.path, "r") as status_file:
                status = json.load(status_file)
        except FileNotFoundError:
            status = {}
            
        status[key] = value
        
        with open(self.path, "w") as status_file:
            json.dump(status, status_file, indent=2)
        

class Pinnacle():
    def __init__(self):
        self.mt5 = Mt5()
        self.ta = TA()
        self.set = Set()
        self.status = Status("status.json")
        
    def start(self, callback_function=None):
        self.mt5.start(callback_function=callback_function, status_update=self.status.set)
    
    def stop(self, callback_function=None):
        self.mt5.stop(callback_function=callback_function, status_update=self.status.set)
        
    def name(self):
        return self.__class__.__name__
    
    
    
    