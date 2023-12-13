
import json
import yaml
import MetaTrader5 as this
import pandas as pd
from datetime import datetime, timedelta
from flask import jsonify
    
class Pinnacle():
    def __init__(self, auth_file):
        self.timeframe_map = {
            '1min': this.TIMEFRAME_M1,
            '5min': this.TIMEFRAME_M5,
            '15min': this.TIMEFRAME_M15,
            '30min': this.TIMEFRAME_M30,
            '1hour': this.TIMEFRAME_H1,
            '4hour': this.TIMEFRAME_H4,
            'daily': this.TIMEFRAME_D1,
            'weekly': this.TIMEFRAME_W1,
            'monthly': this.TIMEFRAME_MN1,
        }
        self.auth_file = auth_file
        self.mt5 = self.Mt5()
        self.get = self.Get()
        self.set = self.Set()
        self.logger = self.Logger()
        self.ta = self.TechnicalAnalysis()
        
    def format_tieframe(self, timeframe):
        return self.timeframe_map.get(timeframe, '')
    
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
    
    class Mt5():
        def __init__(self) -> None:
            self.status = False
            self.id = None
            self.server_name = None
            self.password = None

            
        def name(self):
            return self.__class__.__name__
        
        def login(self, _login=None, _server=None, _password=None):
            this.initialize()
            if _login:
                self.id = _login
            if _server:
                self.server_name = _server
            if _password:
                self.password = _password
            this.login(login=self.id, server=self.server_name, password=self.password)    
        
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
                    
        def get_trading_history(self, mt5_instance, start_date, end_date):
            # Set the time range for the past month
            start_time = datetime.combine(start_date, datetime.min.time())
            end_time = datetime.combine(end_date, datetime.max.time())

            # Get trading history
            history = mt5_instance.history_deals_get(start_time, end_time)

            return history

        def calculate_cumulative_profit(self, data):
            cumulative_profit = 0
            for date, trades in data.items():
                if date == 'initial_balance' or date == 'total_profit':
                    continue
                
                for _, trade_info in trades.items():
                    cumulative_profit += float(trade_info['profit'])

                    # Add the cumulative profit information to the trade
                    trade_info['cumulative_profit_now'] = cumulative_profit

            return data

        def format_trading_history(self, history, _days):
            formatted_data = {}
            
            dayone = datetime.now() - timedelta(days=_days)
            
            formatted_data["initial_balance"] = history[0][13]
            days = []
            for i in range(1, _days + 1):
                day = dayone + timedelta(days=i)
                day = str(day).split(" ")[0]
                days.append(day)
                formatted_data[day] = {}
                
                 
            prof = 0.0
            profits = []
            for day in days:
                for i in range(1, len(history)):
                    trade = history[i]
                    if trade[13] != 0.0:
                        dt = pd.to_datetime(trade[3], unit='ms').replace(microsecond=0).isoformat()
                        dt = dt.replace("T", " ")
                        copy_dt = dt
                        
                        if str(copy_dt).split(" ")[0] == day:
                            
                            
                            newh = self.get_trading_history(this, datetime.now() - timedelta(days=1000), datetime.now())
                            for j in range(1, len(history)):
                                t = newh[j]
                                
                                if t[7] == trade[7] and t[13] == 0.0:
                                    openP = t[10]
                            if openP < trade[10] and trade[13] > 0:
                                typ = "long"
                            else:
                                typ = "short"
                            dt = str(dt).split(" ")[1]
                            if dt not in formatted_data[day]:
                                formatted_data[day][dt] = {}
                                formatted_data[day][dt]["symbol"] = trade[15]
                                formatted_data[day][dt]["size"] = trade[9]
                                formatted_data[day][dt]["open"] = openP
                                formatted_data[day][dt]["close"] = trade[10]
                                formatted_data[day][dt]["type"] = typ
                                formatted_data[day][dt]["profit"] = trade[13]
                                profits.append(trade[13])
                            else:
                                count_ajd = sum(key.count(dt) for key in formatted_data[day].keys())
                                dt = dt + str(count_ajd)
                                formatted_data[day][dt] = {}
                                formatted_data[day][dt]["symbol"] = trade[15]
                                formatted_data[day][dt]["size"] = trade[9]
                                formatted_data[day][dt]["open"] = openP
                                formatted_data[day][dt]["close"] = trade[10]
                                formatted_data[day][dt]["type"] = typ
                                formatted_data[day][dt]["profit"] = trade[13]
                                profits.append(formatted_data[day][dt]["profit"])
                                
                            
            prof = sum(profits)
            profInt = str(prof).split(".")[0]
            profDec = str(prof).split(".")[1]
            profDec = profDec[0:2]
            prof = profInt + "." + profDec
            formatted_data["total_profit"] = prof
            
            return formatted_data


        def get_history(self):
            # Set the time range for the past month
            today = datetime.now()
            end_date = today

            # Initialize MetaTrader 5 connection
            self.login()

            # Get daily trading history
            start_date_daily = (today - timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
            history_daily = self.get_trading_history(this, start_date_daily, end_date)
            daily_formatted_data = self.calculate_cumulative_profit(self.format_trading_history(history_daily, 1))
            print(history_daily)
            # Get monthly trading history
            start_date_monthly = today - timedelta(days=30)
            history_monthly = self.get_trading_history(this, start_date_monthly, end_date)
            monthly_formatted_data = self.calculate_cumulative_profit(self.format_trading_history(history_monthly, 30))

            # Get yearly trading history
            start_date_yearly = today - timedelta(days=365)
            history_yearly = self.get_trading_history(this, start_date_yearly, end_date)
            yearly_formatted_data = self.calculate_cumulative_profit(self.format_trading_history(history_yearly, 365))

            openPos = this.positions_total()
            currentEq = this.account_info().equity

            print(daily_formatted_data)

            formatted_data = {"info": {"open_positions": openPos, "equity": currentEq}, "daily": daily_formatted_data, "monthly": monthly_formatted_data, "yearly": yearly_formatted_data}
            
            # Convert to JSON and print
            with open('history.json', 'w') as history_file:
                json.dump(formatted_data, history_file, indent=4)
        
    class Logger():
        def __init__(self) -> None:
            pass
        
        def R(self):
            return open('logs/bot.log', 'r').read()
        
        def A(self, msg):
            with open('logs/bot.log', 'a') as file:
                file.write(msg + "\n")
        
        def W(self, msg):
            with open('logs/bot.log', 'w') as file:
                file.write(msg + "\n")
        
        def log(self, msg):
            self.A(msg)

        def reset(self):
            with open('logs/bot.log', 'w') as file:
                file.write("Session Started \n----------------\n")

    class TechnicalAnalysis():
        def __init__(self) -> None:
            pass
        
        def name(self):
            return self.__class__.__name__
    
