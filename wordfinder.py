"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    def __init__(self, filename):
        self.file = open(filename).read().split('\n')
        # self.file = filter(None, self.file)
        for word in self.file:
            word = word.strip()
            # print(f"{len(word)} words read")

    def random(self):
        return random.choice(self.file)

# w = WordFinder("/Users/gabbycampos/Desktop/JavaScript_stuff/Springboard/Exercises/python-oo-practice/words.txt")
# print(w.random())


class SpecialWordFinder(WordFinder):
    def special(self):
        for word in self.file:
            # print(word)
            word = word.strip()
            if not word.startswith('#'):
                print(word)


newWord = SpecialWordFinder(
    "/Users/gabbycampos/Desktop/JavaScript_stuff/Springboard/Exercises/python-oo-practice/wordsCopy.txt")
print(newWord.special())
