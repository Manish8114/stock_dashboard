
import pandas as pd
import ta

def calculate_indicators(df):
    df['RSI'] = ta.momentum.RSIIndicator(df['Close']).rsi()
    df['MACD'] = ta.trend.MACD(df['Close']).macd()
    df['CCI'] = ta.trend.cci(df['High'], df['Low'], df['Close'])
    df['ATR'] = ta.volatility.AverageTrueRange(df['High'], df['Low'], df['Close']).average_true_range()
    df['ADX'] = ta.trend.ADXIndicator(df['High'], df['Low'], df['Close']).adx()
    return df[['RSI', 'MACD', 'CCI', 'ATR', 'ADX']].tail(1)
