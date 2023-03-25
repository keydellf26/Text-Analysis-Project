from mediawiki import MediaWiki


wikipedia = MediaWiki()
ManU = wikipedia.page("Manchester United")
print(ManU.title)
print(ManU.content)

def process_site():
    """Makes a histogram that contains the words from a site.
    """
    hist = {}
    fp = ManU.content

    for line in fp.split('\n'):  # got this part from chat gpt ".split('\n')"
        word = line.strip()

        line = line.replace('-', ' ')
        line = line.replace(
            chr(8212), ' '
        )  # Unicode 8212 is the HTML decimal entity for em dash

        for word in line.split():

            # update the dictionary
            hist[word] = hist.get(word, 0) + 1

    return hist

'''
The following 4 lines of code are from 
https://stackabuse.com/removing-stop-words-from-strings-in-python/#usingpythonsnltklibrary

Where I was able to research more about NLTK and install some text documents too
I also used https://www.nltk.org/data.html to import the data
'''
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.tokenize import word_tokenize    



def removestops():

    text = ManU.content
    text_tokens = word_tokenize(text)

    tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]

    return(tokens_without_sw)


'''
The following code came from ChatGPT after asking it to give me 
a random piece of code to add to my orginal code in order to furthur 
analyze the text 


'''
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

def analyze_sentiment():
    sia = SentimentIntensityAnalyzer()
    text = ManU.content
    sentiment_scores = sia.polarity_scores(text)
    return sentiment_scores


def main():

    print()
    print()
    print("Histogram starts below ")
    print()
    print(process_site())
    print()
    print()
    print("Shortened Text Below")
    print()
    print(removestops())
    print()
    print()
    print("Sentiment Analysis Results:")
    print()
    print(analyze_sentiment())




if __name__ == '__main__':
    main()


