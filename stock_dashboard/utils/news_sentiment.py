
from newsapi import NewsApiClient
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

newsapi = NewsApiClient(api_key='e8dd41e46cba4f9da850a46f4395769c')
analyzer = SentimentIntensityAnalyzer()

def fetch_news_and_sentiment(ticker):
    query = f"{ticker} stock India"
    articles = newsapi.get_everything(q=query, language='en', page_size=5)
    news_list = []

    for article in articles['articles']:
        title = article['title']
        sentiment_score = analyzer.polarity_scores(title)['compound']
        sentiment = 'Positive' if sentiment_score > 0.2 else 'Negative' if sentiment_score < -0.2 else 'Neutral'
        news_list.append({
            'title': title,
            'sentiment': sentiment,
            'url': article['url']
        })
    return news_list
