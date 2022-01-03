"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    def __init__(self,path):
        "Reads the file and makes an attribute of a list of those words"
        file = open(path)
        self.word_list=self.read_file(file) 
        print (f"“{len(self.word_list)} words read”")

    def read_file(self,file):
            return [w.strip() for w in file]
    def random(self):
        return random.choice(self.word_list)
        
 
    

    

