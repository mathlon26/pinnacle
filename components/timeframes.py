import MetaTrader5 as mt5
timeframe_map = {
    '1min': mt5.TIMEFRAME_M1,
    '5min': mt5.TIMEFRAME_M5,
    '15min': mt5.TIMEFRAME_M15,
    '30min': mt5.TIMEFRAME_M30,
    '1hour': mt5.TIMEFRAME_H1,
    '4hour': mt5.TIMEFRAME_H4,
    'daily': mt5.TIMEFRAME_D1,
    'weekly': mt5.TIMEFRAME_W1,
    'monthly': mt5.TIMEFRAME_MN1,
}

def T(timeframe):
    return timeframe_map.get(timeframe, '')