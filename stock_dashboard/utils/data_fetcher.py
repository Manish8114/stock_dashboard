
def get_intraday_data(ticker):
    try:
        df = yf.download(ticker + ".NS", period="1d", interval="5m")
        print(f"Data fetched for {ticker}: {df.shape[0]} rows.")
        return df
    except Exception as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()

