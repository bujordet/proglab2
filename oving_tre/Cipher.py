import Person
import crypto_utils

__author__ = "Morten Bujordet"

class Cipher(object):
    """docstring for """
    def __init__(self):
        self.alfabetet = ["A","B","C","D","E","F","G","H"]
        self.tegn = 8

    def encode(self, klarTekst):

        return encode


    def decode(self, kryptTekst):

        return decode


    def verify(self, klarTekst):
        cipherTekst = self.encode(klarTekst)

        #print(cipherTekst)
        return self.decode(cipherTekst) == klarTekst

    def generate_keys(self):
        return key

class Caesar(Cipher):
    def __init__(self, key):
        super().__init__()
        self.key = key

    def encode(self, klarTekst):
        kodet_tekst = ""
        for symbol in klarTekst:
            orginal = self.alfabetet.index(symbol)
            tall = orginal + self.key
            if (tall >= self.tegn):
                tall = tall%self.tegn
            kodet_tekst += self.alfabetet[tall]
        return kodet_tekst

    def decode(self, kryptTekst):
        dekodet_tekst = ""
        for symbol in kryptTekst:
            orginal = self.alfabetet.index(symbol)
            tall = orginal - self.key
            if (tall < 0):
                tall = (tall + self.tegn)%self.tegn
            dekodet_tekst += self.alfabetet[tall]
        return dekodet_tekst

    def generate_keys(self):
        Person.Sender(self.key)
        Person.Reciver(self.key)

class Multiplicative(Cipher):
    def __init__(self, key):
        super().__init__()
        self.key = key

    def encode(self, klarTekst):
        kodet_tekst = ""
        for symbol in klarTekst:
            orginal = self.alfabetet.index(symbol)
            tall = orginal * self.key
            if (tall >= self.tegn):
                tall = tall%self.tegn
            kodet_tekst += self.alfabetet[tall]
        return kodet_tekst

    def decode(self, klarTekst):
        kodet_tekst = ""
        for symbol in klarTekst:
            orginal = self.alfabetet.index(symbol)
            tall = ((orginal * self.key)%self.tegn)*crypto_utils.modular_inverse(self.key, self.tegn)%self.tegn
            #if (tall >= self.tegn):
            #    tall = tall%self.tegn
            kodet_tekst += self.alfabetet[tall]
        return kodet_tekst
