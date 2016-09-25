__author__ = "Morten Bujordet"

import Cipher

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
