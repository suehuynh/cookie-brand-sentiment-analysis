# Piechart for distribution of positive, neutral, and negative
fig, axes = plt.subplots(1, len(brands), figsize=(6*len(brands), 6))

if len(brands) == 1:
    axes = [axes]

for ax, b in zip(axes, brands):
    sentiment_counts = df[df["brand"]==b]["sentiment"].value_counts()

    ax.pie(
        sentiment_counts,
        labels=sentiment_counts.index,
        autopct="%1.1f%%",
        startangle=140,
        colors=["#93c47d", "#ffe599", "#ff9999"],
        textprops={"fontsize": 11}
    )
    ax.set_title(f"{b}\nSentiment Distribution", fontsize=14, fontweight="bold")

plt.tight_layout()
plt.show()

# Sentiment score distribution
brand_palette = {
    "Insomnia Cookies": "#693EFE",   
    "Levain Bakery": "#6395EE",      
    "Crumbl Cookies": "#FF6FA5"      
}

plt.figure(figsize=(10,6))
sns.histplot(
    data=df, 
    x="sentiment_score", 
    hue="brand", 
    kde=True, 
    bins=30, 
    element="step",
    stat="density",
    palette = brand_palette,
    common_norm=False
)
plt.title("Sentiment Score Distribution by Brand", fontsize=14, fontweight="bold")
plt.xlabel("Sentiment Score (VADER compound)")
plt.ylabel("Density")
plt.show()

# Violin chart for score distribution
plt.figure(figsize=(8,6))
sns.violinplot(data=df, x="brand", y="sentiment_score", palette=brand_palette, inner="quartile")
plt.title("Sentiment Score Distribution by Brand", fontsize=14, fontweight="bold")
plt.ylabel("Sentiment Score")
plt.xlabel("Brand")
plt.show()

# Sentiment score overtime
time_sentiment = (
    df
    .set_index("created_at")
    .groupby(["brand", "media"])
    .resample("M")["sentiment_score"]
    .mean()
    .reset_index()
)
plt.figure(figsize=(12,6))
sns.lineplot(
    data=time_sentiment, 
    x="created_at", 
    y="sentiment_score", 
    hue="brand", 
    palette=brand_palette,
    linewidth=2.5
)

plt.axhline(0, color="gray", linestyle="--", linewidth=1)
plt.title("Sentiment Score Over Time", fontsize=14, fontweight="bold")
plt.xlabel("Date")
plt.ylabel("Average Sentiment Score")
plt.legend(title="Brand")
plt.show()
