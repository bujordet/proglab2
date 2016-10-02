__author__ = "Ole Håkon Ødegård"
from sys import stdin
import traceback

class Node:
    def __init__(self):
        self.barn = {}
        self.is_end = False


class WordList:

    def __init__(self, filepath: str = "english_words.txt"):
        self.path = filepath
        self.top_node = Node()
        self.build(self.path)

    def build(self, word_list):
        for word in self.get_word_list():
            node = self.top_node
            for i in range(len(word)):
                if node.barn.get(word[i]) is None:
                    node.barn[word[i]] = Node()
                node = node.barn[word[i]]
            node.is_end = True

    def __contains__(self, text):
        def check_word(word):
            node = self.top_node
            for l in word:
                if node.barn.get(l) is None:
                    return False
                node = node.barn[l]
            return node.is_end

        words = text.split()
        for w in words:
            if not check_word(w.strip()):
                return False

        return True

    def get_word_list(self) -> list:
        return list(open(self.path, "r+").read().splitlines())
