from textblob import TextBlob
from TheHindu import hindu
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def find_sentiment(news_title, news):
    news = TextBlob(news)
    sentiments = []
    for sentence in news.sentences:
        sentiment = sentence.sentiment
        for metric in sentiment:
            sentiments.append(metric)
    polarity_data = []
    subjective_data = []
    for k in range(len(sentiments)):
        if k%2==0:
            polarity_data.append(sentiments[k])
        else:
            subjective_data.append(sentiments[k])
    polarity_avg = cal_avg(polarity_data)
    subjectivity_avg = cal_avg(subjective_data)

    # Displays the sentiment that relates to the averages on the console.
    print()
    print("FINAL ANALYSIS")
    print("----------------------------------")
    print("NEWS:",news_title)
    print("Polarity: " ,polarity_avg, cal_sentiment(polarity_avg, "polarity"))
    print("Subjectivity: ", subjectivity_avg, cal_sentiment(subjectivity_avg, "subjectivity"))

def cal_avg(list):
    return sum(list)/len(list)

def cal_sentiment(sentiment, type):
    sentiment_category = ""
    if type == "polarity":
        if sentiment > 0.5:
            sentiment_category = 'positive.'
        elif sentiment > 0.3:
            sentiment_category = "Fairly positive."
        elif sentiment > 0.1:
            sentiment_category = "Slightly positive."
        elif sentiment < -0.5:
            sentiment_category = "negative."
        elif sentiment < -0.3:
            sentiment_category = "Fairly negative."
        elif sentiment < 0:
            sentiment_category = "slightly negative."
        else:
            sentiment_category = "Neutral."
        return sentiment_category
    elif type == "subjectivity":
        if sentiment > 0.75:
            sentiment_category = "Extremely subjective."
        elif sentiment > 0.5:
            sentiment_category = "Fairly subjective."
        elif sentiment > 0.3:
            sentiment_category = "Fairly objective."
        elif sentiment > 0.1:
            sentiment_category = "Extremely objective."
        return sentiment_category
    else:
        print("Invalid Input.")

news_articles = hindu()

for i,j in news_articles.items():
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(j)
    filtered = [w for w in word_tokens if not w.lower() in stop_words]
    filtered_para = ' '.join(filtered)
    #print(filtered_para)
    find_sentiment(i,filtered_para)