import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
nltk.download('stopwords')
nltk.download('wordnet')
stopwords = set(stopwords.words('english'))
class ProcessText:
    """
    Process fiven text, to fit model specs:
     - Remove stop words
     - Lower
     - Remove special characters
    """

    def __init__(self):
        self.stopwords = stopwords
        self.lm = WordNetLemmatizer()

    def preprocess(self, txt: str)->str:
        """
        Convert Process the text
        :param txt: Paper text
        :return: manipulated text
        """
        txt = txt.lower()
        txt = re.sub("&lt;/?.*?&gt;", " &lt;&gt; ", txt)  # Remove HTML tags
        txt = re.sub("(\\d|\\W)+", ' ', txt)
        txt = txt.split()
        txt = [wrd for wrd in txt if
               wrd not in self.stopwords and len(wrd) >= 3]  # Remove stopwords, keep only words that have 3 or more letters
        txt = [self.lm.lemmatize(wrd) for wrd in txt]
        return ' '.join(txt)

