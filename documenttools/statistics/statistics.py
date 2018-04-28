import sys, re, os

try: 
    from textstat.textstat import textstat
except ImportError: 
    print 'You need to install textstat first. Try sudo pip install textstat'
    sys.exit()


try: 
    from textblob import TextBlob
    from textblob.sentiments import NaiveBayesAnalyzer
except ImportError: 
    print 'You need to install textblob first. Try sudo pip install textblob'
    sys.exit()

from documenttools.files.readers import FileReader


class DocumentStatistics: 
    @staticmethod
    def get_sentiment(content): 
        blob = TextBlob(content)
        polarity, subjectivity = blob.sentiment

        blob = TextBlob(content, analyzer=NaiveBayesAnalyzer())
        classification, p_pos, p_neg = blob.sentiment.classification, blob.sentiment.p_pos, blob.sentiment.p_neg
        
        return [round(polarity, 4), round(subjectivity, 4), classification, round(p_pos, 4), round(p_neg, 4)]

    def __init__(self, input_file, keywords): 
        self.file = input_file
        self.keywords = keywords
    
    def get_keyword_frequency(self, content): 
        frequencies = {}

        for keyword in self.keywords: 
            frequencies[keyword] = len(re.findall(r'{}'.format(keyword.lower()), content))
        return sorted([(kw, frequencies[kw]) for kw in frequencies], key=lambda x: x[0])

    def get_statistics(self, f, content): 
        content = content.lower()
        
        reading_level = textstat.flesch_kincaid_grade(content)
        word_count = textstat.lexicon_count(content)
        keyword_frequency = map(lambda x: x[1], self.get_keyword_frequency(content))
        sentiment = DocumentStatistics.get_sentiment(content)
        return [f, reading_level, word_count] + keyword_frequency + sentiment

    def compute(self): 
        # reader = FileReader(self.file)
        content = self.file[1] # reader.read()
        return self.get_statistics(self.file[0], content)
        