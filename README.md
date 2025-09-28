# Sentiment & Media Analysis of Cookie Brands
*Crumbl Cookies, Insomnia Cookies, and Levain Bakery*

# Research Question

How do public perceptions of major cookie brands—Crumbl, Insomnia, and Levain—differ across consumer reviews, social media discussions, and news coverage in terms of sentiment, review volume, and brand identity?

# Abstract

This project analyzes consumer sentiment and media representation of three cookie brands: Crumbl Cookies, Insomnia Cookies, and Levain Bakery. Using data from Reddit and News API, I collected reviews and articles to perform sentiment analysis, word cloud visualization, and trend analysis over time.

Findings reveal distinct brand dynamics: Crumbl generates the most media buzz but also polarizing sentiment, Insomnia maintains steady positivity tied to convenience and consistency, while Levain enjoys overwhelmingly positive reception due to product excellence and heritage. This study highlights how consumer narratives shape brand reputation in both digital and traditional media.

# Data Sources
- Reddit API (PRAW): User discussions across food and brand-related subreddits
- NewsAPI: Online news articles mentioning each brand

# Methodology
1. Data Collection
- Pulled Reddit posts and comments mentioning each brand
- Queried NewsAPI for relevant brand mentions in articles

2. Data Preprocessing
- Cleaned text (lowercasing, stopword removal, tokenization)
- Extracted metadata (date, brand, source)
- Converted timestamps (created_utc, publishedAt) to datetime format

3. Sentiment Analysis
- Applied pre-trained sentiment classifier (VADER/TextBlob)
- Classified reviews into positive, neutral, or negative
- Calculated sentiment scores for distribution analysis

4. Visualization
- Word clouds: Most frequent terms per brand
- Pie charts: Sentiment distribution by brand
- Violin plots: Sentiment score distributions
- Time series plots: Sentiment score trends over time

5. Results (more details with plots)

Word Cloud Insights
- Crumbl: Strong associations with sugar and weekly flavor drops → polarizing buzz
- Insomnia: Mentions of order, open, and Krispy Kreme → convenience-driven identity
- Levain: Strongly tied to chocolate chip walnut cookie and NYC → premium, heritage-based branding

Sentiment Distribution
- Crumbl: 41% positive, 36% neutral, 23% negative
- Insomnia: 50% positive, 35% neutral, 15% negative
- Levain: 51% positive, 42% neutral, 7% negative

Sentiment Score Trends
- Crumbl: Highly fluctuating, tied to viral menu releases
- Insomnia: Steady sentiment, fewer extremes
- Levain: Strong upward trajectory with expansion beyond NYC
6. Discussion
- Crumbl is the most talked-about and polarizing brand, thriving on attention but facing pushback on health and flavor variety.
- Insomnia balances visibility and consistency, appealing to its target demographic with reliability rather than hype.
- Levain enjoys the most favorable sentiment per review, leveraging product excellence and brand heritage to create an almost cult-like following.

# Limitations
- Sample size: Limited to scraped data, may not reflect the full population of reviews
- Bias in sentiment models: Pre-trained classifiers may misinterpret sarcasm or brand-specific slang
- Temporal skew: NewsAPI returns more recent articles, possibly underrepresenting historical coverage

# Next Steps
- Expand data collection to include food reviews from Google Reviews, Yelp, UberEats
- Perform topic modeling (LDA/BERT) to uncover deeper themes beyond sentiment
