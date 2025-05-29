
import yfinance as yf

def get_intraday_data(ticker):
    df = yf.download(ticker + ".NS", period="1d", interval="5m")
    return df
