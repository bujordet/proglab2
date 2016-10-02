__author__ = "Morten Bujordet"

import Cipher
from sys import stdin

class Person(object):
    """docstring for """
    def __init__(self, cipher):
        super(self).__init__()
        self.key = key
        self.cipher = cipher

    def set_key(self, key):
        self.key = key

    def get_key(self):
        return self.key

    def operate_cipher(self):
        return text

class Sender(Person):

    def operate_cipher(self):
        #Encoder en ren tekst
        return coded_text

class Reciver(Person):
    def operate_cipher(self):
        #Behandler en kodet tekst og decoder denne.
        return decoded_text

class Hacker(Person):
    def __init__(self, kodet_tekst):
        self.kodet_tekst = kodet_tekst

    def operate_cipher(self):
        svar = False

        for n in range(Cipher.tegn):
            dekodet_tekst = Cipher.Caesar(n).decode(self.kodet_tekst)
            svar = self.check_wordlist(dekodet_tekst)
            if (svar == True):
                return dekodet_tekst

    def check_wordlist(self, dekodet_tekst):
        for line in stdin:
            word = line.split()
            if (word == dekodet_tekst):
                return True
        return False
