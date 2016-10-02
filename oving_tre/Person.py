__author__ = "Morten Bujordet"

import Cipher
import crypto_utils
import ordliste
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
        self.ordliste = ordliste.WordList()

    def operate_cipher(self):
        svar = False

        for n in range(Cipher.tegn):
            """dekodet_tekst = Cipher.Caesar(n).decode(self.kodet_tekst)
            print(dekodet_tekst)"""
            oppsett = Cipher.Caesar(n)
            decode = oppsett.decode(self.kodet_tekst)
            #print(decode)
            check = self.ordliste.__contains__(decode)
            if (check):
                return True
        return False
