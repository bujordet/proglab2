__author__ = "Morten Bujordet"

import Cipher
import crypto_utils
import ordliste
import hack_operate
from sys import stdin

class Person(object):
    """docstring for """
    def __init__(self, key, cipher):
        super(self).__init__()
        self.key = key

    def set_key(self, key):
        self.key = key

    def get_key(self):
        return self.key

    def operate_cipher(self):
        return text

class Sender(Person):

    def operate_cipher(self):
        return coded_text

class Reciver(Person):
    def operate_cipher(self):
        #Behandler en kodet tekst og decoder denne.
        return decoded_text

class Hacker:
    def __init__(self, kodet_tekst):
        self.kodet_tekst = kodet_tekst
        self.ordliste = ordliste.WordList()

    def operate_cipher(self):
        caesar = hack_operate.Hacker(self.kodet_tekst).caesar_hack()
        multiplicative = hack_operate.Hacker(self.kodet_tekst).multiplicative_hack()
        affine = hack_operate.Hacker(self.kodet_tekst).affine_hack()
        unbrakable = hack_operate.Hacker(self.kodet_tekst).unbrakable_hacker()
