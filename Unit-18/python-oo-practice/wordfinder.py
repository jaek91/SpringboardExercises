import random

"""Word Finder: finds random words from a dictionary."""

class WordFinder:

    def __init__(self, path):
       """Read list of words from path and returns # of items read"""
       word_list = open(path, "r")
       self.words = self.read_text_file(word_list)
       print(f"{len(self.words)} words read from file!")

    def read_text_file(self, file):
        """reads in words from the txt file line by line and stores them in a list"""
        wordlist = [line.rstrip() for line in file]
        return wordlist

    def random(self):
        """returns a random word from the list of words"""
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Special version of word finder where we exclude blank white spaces/comments

    >>> s = SpecialWordFinder("fruitsandveggies.txt")
    6 words read from file!
    >>> s.random() in ["mangoes","bananas","blueberries","carrots", "broccoli", "squash"]
    True
    """
    def read_text_file(self, file):
       """reads in words from file while skipping blank spaces/comments"""
       res = [line.strip() for line in file if line.strip() and not line.startswith("#")]
       return res
      

