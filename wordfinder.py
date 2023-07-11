"""Word Finder: finds random words from a dictionary."""
import random


# file = open("words.txt", "r")
# random_line = random.choice(file)

class WordFinder:
    
    def __init__(self,file_path):
        self.file_path = file_path
        self.words = []

    def read_file(self):
        with open(self.file_path, 'r') as file:
            self.words = file.readlines()

    def random_line(self):
        if not self.words:
            self.read_file()
        return random.choice(self.words)

random_word = WordFinder(file_path="words.txt")
print(random_word.random_line())