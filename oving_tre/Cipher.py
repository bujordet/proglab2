import Person
import crypto_utils

__author__ = "Morten Bujordet"

class Cipher(object):
    """docstring for """
    def __init__(self):
        self.alfabetet = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*',\
         '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',\
         ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',\
         'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',\
         'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f',\
         'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',\
         'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']

        self.tegn = 95

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
        #if (self.check_key() is False):
            #print("Key is not 1to1")
        kodet_tekst = ""
        for symbol in klarTekst:
            orginal = self.alfabetet.index(symbol)
            tall = orginal * self.key
            if (tall >= self.tegn):
                tall = tall%self.tegn
            kodet_tekst += self.alfabetet[tall]
        return kodet_tekst

    def decode(self, kryptTekst):
        #print(self.tegn)
        #print(self.key)
        klar_tekst = ""
        for symbol in kryptTekst:
            orginal = self.alfabetet.index(symbol)
            m = crypto_utils.modular_inverse(self.key, self.tegn)
            #print(m)
            ny_key = (orginal*m)%self.tegn
            klar_tekst += self.alfabetet[ny_key]
        return klar_tekst

    def check_key(self):
        m = crypto_utils.modular_inverse(self.key, self.tegn)
        return (self.key*m == 1%self.tegn)

class Affine(Cipher):
    def __init__(self, key):
        super().__init__()
        self.keyone = key[0]
        self.keytwo = key[1]

    def encode(self, klar_tekst):
        kodet_tekst = Multiplicative(self.keyone).encode(klar_tekst)
        #print(kodet_tekst)
        resultat = Caesar(self.keytwo).encode(kodet_tekst)
        return resultat

    def decode(self, kodet_tekst):
        steg_en = Caesar(self.tegn - self.keytwo).encode(kodet_tekst)
        dekodet_tekst = Multiplicative(self.keyone).decode(steg_en)
        return dekodet_tekst

class Unbrakable(Cipher):
    def __init__(self, keyword):
        super().__init__()
        self.keyword = keyword

    def encode(self, klar_tekst):
        kodet_tekst = ""
        count = 0
        for letter in klar_tekst:
            verdi_tekst = self.alfabetet.index(letter)
            verdi_kodeord = self.alfabetet.index(self.keyword[count])
            totalverdi = verdi_kodeord + verdi_tekst
            if (totalverdi >= self.tegn):
                totalverdi = totalverdi%self.tegn
            kodet_tekst += self.alfabetet[totalverdi]
            if (count == len(self.keyword)-1):
                count = 0

        return kodet_tekst

    def decode(self, kodet_tekst):
        dekodet_tekst = ""
        lureord = []
        for letter in self.keyword:
            verdi_kodeord = self.alfabetet.index(letter)
            verdi_lureord = (self.tegn - verdi_kodeord)%self.tegn
            lureord.append(verdi_lureord)
        x = 0
        for character in kodet_tekst:
            verdi_tekst = self.alfabetet.index(character)
            tilbake_verdi = verdi_tekst + lureord[x]
            if (tilbake_verdi >= self.tegn):
                tilbake_verdi = tilbake_verdi%self.tegn
            dekodet_tekst += self.alfabetet[tilbake_verdi]
            if (x == len(lureord)-1):
                x = 0

        return dekodet_tekst
