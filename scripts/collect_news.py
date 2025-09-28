# Install requests
!pip install requests
import requests
import pandas as pd

brands = ["Crumbl Cookies", "Insomnia Cookies", "Levain Bakery"]
NEWS_API_KEY = "NEWSAPIKEY"

def fetch_news(query, page_size=50):
    url = f"https://newsapi.org/v2/everything?q={query}&language=en&pageSize={page_size}&apiKey={NEWS_API_KEY}"
    response = requests.get(url).json()
    
    articles = []
    for article in response.get("articles", []):
        articles.append({
            "brand": query,
            "source": article["source"]["name"],
            "title": article["title"],
            "description": article["description"],
            "url": article["url"],
            "publishedAt": article["publishedAt"]
        })
    return pd.DataFrame(articles)

news_df = pd.concat([fetch_news(b) for b in brands])
news_df['review'] = news_df['title'] + ' ' + news_df['description']
news_df.to_csv("news_mentions.csv", index=False)
news_df.head()
