__author__ = "Morten Bujordet"

import Cipher
import crypto_utils
import ordliste
import Person
from sys import stdin


class Hacker(object):
    def __init__(self, kodet_tekst, filepath: str = "english_words.txt"):
        self.path = filepath
        self.kodet_tekst = kodet_tekst
        self.ordliste = ordliste.WordList()

    def caesar_hack(self):
        for n in range(1, Cipher.tegn):
            oppsett = Cipher.Caesar(n)
            decode = oppsett.decode(self.kodet_tekst)
            if(self.ordliste.__contains__(decode)):
                print("Caesar:", decode)
                return True
        return False

    def multiplicative_hack(self):
        #print("inne")
        for n in range(1, Cipher.tegn):
            #print(n)
            oppsett = Cipher.Multiplicative(n)
            decode = oppsett.decode(self.kodet_tekst)
            if(self.ordliste.__contains__(decode)):
                print("Multiplicative:",decode)
                return True
        return False

    def affine_hack(self):
        for n in range(1, Cipher.tegn):
            for a in range(1, Cipher.tegn):
                oppsett = Cipher.Affine((n,a))
                decode = oppsett.decode(self.kodet_tekst)
                if(self.ordliste.__contains__(decode)):
                    print("Affine:",decode)
                    return True
        return False

    def unbrakable_hacker(self):

        for word in self.get_word_list():
            oppsett = Cipher.Unbrakable(word)
            decode = oppsett.decode(self.kodet_tekst)
            if (self.ordliste.__contains__(decode)):
                print("Unbrakable:",decode)
                print("Keyword:", word)
                return True
        return False

    def get_word_list(self) -> list:
        return list(open(self.path, "r+").read().splitlines())
