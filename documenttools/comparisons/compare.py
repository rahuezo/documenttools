import sys 

try: 
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
except ImportError: 
    print "You need to install sklearn. Try, sudo pip install sklearn"
    sys.exit()

try: 
    from networktools.files.readers import FileReader
except ImportError: 
    print "You need to install networktools."
    sys.exit()


SHINGLE_SIZE = 3
ONLINE = True


def get_cosine_similarity(content1, content2):
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform((content1, content2))
    cosim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)[0][-1]
    return round(cosim, 4)


def get_shingles(content, size):
    buff = content.lower()

    for i in range(0, len(buff) - size + 1):
        output = buff[i:i + size]
        yield output


def compute_jaccard(set1, set2):
    x = len(set1.intersection(set2))
    y = len(set1.union(set2))
    return x / float(y)


def get_jaccard_similarity(content1, content2):
    shingles_1 = set(get_shingles(content1, size=SHINGLE_SIZE))
    shingles_2 = set(get_shingles(content2, size=SHINGLE_SIZE))
    jasim = compute_jaccard(shingles_1, shingles_2)
    return round(jasim, 4)
    

def compare_documents(content1, content2):
    cosim = get_cosine_similarity(content1, content2)
    jasim = get_jaccard_similarity(content1, content2)
    return cosim, jasim


class DocumentComparison: 
    """
    This class is used to compare a list of files against each other. The comparison 
    yields the cosine and Jaccard similarity betweet two files.
    """
    def __init__(self, files):
        self.files = files

    def compare(self): 
        """
        This function compares a list of files against each other.

        Args:
            self.files: list of files to compare.

        Returns: 
            Comparisons list: Filename1, Filename2, Cosine Similarity, Jaccard Similarity
        """ 
        comparisons = []

        for i in xrange(len(self.files)): 
            for j in xrange(i + 1, len(self.files)): 
                f1, f2 = self.files[i], self.files[j]                
                cosim, jasim = compare_documents(f1[1], f2[1])                
                comparisons.append((f1[0], f2[0], cosim, jasim))

        return comparisons