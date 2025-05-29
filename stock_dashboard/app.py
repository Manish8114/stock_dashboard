
import streamlit as st
from utils.data_fetcher import get_intraday_data
from utils.indicators import calculate_indicators
from utils.news_sentiment import fetch_news_and_sentiment

st.set_page_config(page_title="Stock Analysis Tool", layout="wide")
st.title("📊 Intraday Stock Analysis")

ticker = st.text_input("Enter NSE Stock Symbol (e.g., ITC)", "ITC")

if ticker:
    df = get_intraday_data(ticker)
    
    if df.empty or ('Close' not in df.columns) or (df['Close'].isna().all()):
        st.error("⚠️ Failed to fetch valid data for the ticker. Please try another symbol.")
    else:
        # Only calculate and display indicators if data is valid
        indicators = calculate_indicators(df)

        st.subheader("🔧 Technical Indicators")
        st.write(indicators)

        # Add other sections here (e.g., plots, support/resistance, etc.)

    st.subheader("📈 Price Chart")
    st.line_chart(df['Close'])

    st.subheader("📰 News & Sentiment")
    for news in news_data:
        st.markdown(f"**{news['title']}**")
        st.markdown(f"*Sentiment: {news['sentiment']}*")
        st.markdown(f"[Read more]({news['url']})")
