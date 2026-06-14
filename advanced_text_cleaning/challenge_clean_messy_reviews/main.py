import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

nltk.download('punkt_tab', quiet=True)

reviews = [
    "AMAZING product!!!!! 😍😍 #best",
    "Terrible service... waited soooo long :(",
    "Loved it!!! Will buy again 100%",
    "@shop Great quality, really really good!",
    "Meeehhhhh... not what I expected."
]

stopwords = ["the", "a", "an", "and", "is", "are", "to", "will", "what", "again"]

stemmer = PorterStemmer()
cleaned_reviews = []  # Initializing list

for review in reviews:
    # Lowercase
    text = review.lower()

    # Remove emojis, hashtags, mentions
    text = re.sub(r"[#@][\w_]+|[\U0001F600-\U0001F64F]", "", text)

    # Normalize characters repeated 3+ times
    text = re.sub(r"(.)\1{2,}", r"\1", text)

    # Tokenize
    tokens = word_tokenize(text)

    # Removing stopwords
    tokens = [t for t in tokens if t not in stopwords]

    # Apply stemming
    tokens = [stemmer.stem(t) for t in tokens]

    print(tokens)
    cleaned_reviews.append(" ".join(tokens))