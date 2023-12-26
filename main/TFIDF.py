import numpy as np

class TFIDFVectorizer:
    
    def __init__(self):
        self.corpus = {}        # dictionary {string : int}
        self.documents = []     # list of documents represented by {"tokens" : {string : int}, "length": int}
    
    def addDoc(self, tokens):
        """
        Populates the corpus and documents. Corpus has unique tokens and respective total counts.
        
        param tokens: list of non-unique tokens
        type tokens: list(string)
        """
        
        new_doc = {"tokens":{}, "length":len(tokens)}
        
        for token in tokens:
            if token in self.corpus:
                self.corpus[token] += 1
            else:
                self.corpus[token] = 1
            
            if token in new_doc["tokens"]:
                new_doc["tokens"][token] += 1
            else:
                new_doc["tokens"][token] = 1
        
        self.documents.append(new_doc)
    
    
    def getTF(self):
        """
        Returns term frequencies of each word in every document.
        
        rtype: np.array(int) (2d)
        """
        
        ret = []
        for token in self.corpus:
            cur_vector = []
            for doc in self.documents:
                if (token in doc["tokens"]):
                    cur_vector.append(doc["tokens"][token] / doc["length"])
                else:
                    cur_vector.append(0)
            
            ret.append(cur_vector)
            
        return np.array(ret)
    
    
    def getIDF(self):
        """
        Returns inverse document frequency of each token.
        
        rtype: np.array(int) (2d)
        """
        
        ret = []
        for token in self.corpus:
            num_doc = 0
            
            for doc in self.documents:
                if (token in doc["tokens"]):
                    num_doc += 1
            idf = np.log(len(self.documents) / num_doc)
            
            new_vector = [idf for i in range(len(self.documents))]
            ret.append(new_vector)
        
        return np.array(ret)
        
        
    def getTFIDF(self):
        """
        Returns vector representations of each word.
        
        rtype: np.array(int) (2d)
        """
        
        return np.multiply(self.getTF(), self.getIDF())
