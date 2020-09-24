"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    def __init__(self, filename):
        self.file = open(filename).read().split()
        for word in self.file:
            word = word.strip()
            print(f"{len(word)} words read")


    def random(self):
        return random.choice(self.file)

# w = WordFinder("/Users/gabbycampos/Downloads/python-oo-practice/words.txt")
# print(w.random())
class SpecialWordFiner(WordFinder):
    def __init__(self, filename):
        super().__init__(filename)

    def special(self):
        for word in self.file:
            if word is not word.startswith('#'):
                return word

newWord = SpecialWordFiner("/Users/gabbycampos/Downloads/python-oo-practice/wordsCopy.txt")
print(newWord.random() in ["pear", "carrot", "kale"])
