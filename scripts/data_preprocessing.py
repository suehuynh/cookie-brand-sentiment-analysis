import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Text Data
nltk.download("stopwords")
nltk.download("wordnet")

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    text = re.sub(r"http\S+|www\S+", "", text)  # remove links
    text = re.sub(r"[^a-zA-Z\s]", "", text)     # remove punctuation/numbers
    text = text.lower()
    tokens = text.split()
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return " ".join(tokens)

reddit_df['clean_review'] = reddit_df['review'].apply(clean_text)
news_df['clean_review'] = news_df['review'].apply(clean_text)

# Datetime Data
# Convert Reddit epoch to datetime (already timezone-naive)
reddit_df["created_at"] = pd.to_datetime(reddit_df["created_utc"], unit="s")

# Convert News publishedAt to datetime and convert to UTC, then make timezone-naive
news_df["created_at"] = pd.to_datetime(news_df["publishedAt"]).dt.tz_convert('UTC').dt.tz_convert(None)

reddit_df["media"] = "Reddit"
news_df["media"] = "News"

df = pd.concat([reddit_df, news_df])
df = df[['brand', 'clean_review', 'created_at', 'media']]
