import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk import FreqDist
import string

# Sample text data (same as Day 5)
texts = [
    "Hello, World! This is a sample text.",
    "AI is transforming the world!!!",
    "Python is great for NLP... Let's learn!"
]

def preprocess_text(text):
    text=text.lower()
    text=text.translate(str.maketrans("","",string.punctuation))
    tokens = word_tokenize(text)

    return tokens

all_tokens = []

for text in texts:
    tokens = preprocess_text(text)
    all_tokens.extend(tokens)

#calculate word frequency
freq_dist = FreqDist(all_tokens)

print("Word frquency:",freq_dist)

#create DataFrame
df=pd.DataFrame(list(freq_dist.items()),columns=['word','frequency'])

#sort by frequency
df=df.sort_values(by='frequency',ascending=False)

#save to csv file

df.to_csv('assignments/word_frequencies.csv',index=False)

#print result

print("Final result :\n",df)