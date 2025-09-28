sia = SentimentIntensityAnalyzer()
df["sentiment_score"] = df["clean_review"].apply(lambda x: sia.polarity_scores(x)["compound"])
df["sentiment"] = df["sentiment_score"].apply(lambda x: "positive" if x > 0.05 else ("negative" if x < -0.05 else "neutral"))
