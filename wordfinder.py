"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    def __init__(self, filename):
        # with open(filename) as f:
        #     for line in f:
        #         line = line.strip()
        #         print(f"{len(self.words)} words read")

        # filename = open("/usr/share/dict/words")
        file = open(filename)
        for word in file:
            word = word.strip()
            print(f"{len(word)} words read")
      
    

    def random(self):
        return random.choice(word)

w = WordFinder("/Users/gabbycampos/Downloads/python-oo-practice/words.txt")
print(w.random())
