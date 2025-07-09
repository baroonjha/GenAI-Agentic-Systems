import pandas as pd
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
import string

# Ensure 'punkt' is downloaded before tokenization
# nltk.download('punkt', quiet=True)

## Text pre-processing 

#Lowercasing 
text = "Hello <p>World!</p> This is a Text Preprocessing Example.,<a> link </a> with some HTML tags."

lowercase =text.lower()


# print("Lowercase:", lowercase)

def remove_html_tags(text):
    import re
    # Regular expression to match HTML tags
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

# print("Remove HTML tags:", remove_html_tags(lowercase))

## url removal
url_text = "Visit https://example.com or www.example.com for more info. Check out our site at https://example.com or http://blog.example.com!"
def remove_urls(text):
    import re
    # Regular expression to match URLs
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return url_pattern.sub('', text)

# print("Remove URLs:", remove_urls(url_text))

## Punctuation removal
def remove_punctuation(text):   
    return text.translate(str.maketrans('', '', string.punctuation))


# Sample text data
texts = [
    "Hello, World! This is a sample text.",
    "AI is transforming the world!!!",
    "Python is great for NLP... Let's learn!"
]

def preprocess_text(text):
    text=text.lower()
    text=text.translate(str.maketrans('','',string.punctuation))

    #tokenize the text
    tokens=word_tokenize(text)
    return tokens

#applying processing
processed_texts = [preprocess_text(text) for text in texts]

print("processed_texts:",processed_texts)

#createdata frame
df = pd.DataFrame({
    'original_text':texts,
    'processed_tokens':processed_texts
})

print("DataFrame is :\n",df)


df.to_csv('mini-projects/processed_texts.csv',index=False)

print("Processed DataFrame:\n",df)