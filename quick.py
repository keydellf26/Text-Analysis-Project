import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.tokenize import word_tokenize

def removestops():
    text = ManU.content
    text_tokens = word_tokenize(text)

    tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]

    return tokens_without_sw

print("Shortened Text Below")
print()
print(removestops())