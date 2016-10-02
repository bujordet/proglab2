#!/usr/bin/env python3

__author__ = "Morten Bujordet"
import Cipher
import crypto_utils
import Person
import random
from sys import stdin


def generate_koding_keys():
    p = crypto_utils.generate_random_prime(8)
    q = crypto_utils.generate_random_prime(8)
    n = p*q
    phi = (p-1)*(q-1)
    e = random.randint(3, phi-1)
    d = crypto_utils.modular_inverse(e, phi)
    while d is -1:
        e = random.randint(3, phi-1)
        d = crypto_utils.modular_inverse(e, phi)
    return (n,e,d)

class main():
    n = 0
    kodet_tekst = ""
    #dic = {"Caesar": Cipher.Caesar(n), "Multiplicative": Cipher.Multiplicative(n), "Affine": Cipher.Affine(n), "Unbrakable": Cipher.Unbrakable(n)}
    all_cipher = ["Caesar", "Multiplicative", "Affine", "Unbrakable"]
    tekst = input("Write text to be decoded: ")
    print("Choose one of the ciphers below")
    for element in all_cipher:
        print(all_cipher.index(element) + 1, ":", element)

    cipher_to_use = input("Choose by write one of the numbers above: ")
    if (cipher_to_use == "1"):
        n = int(input("Write your key (n): "))
        caesar = Cipher.Caesar(n)
        #tekst = tekst.split()
        #for word in tekst:
        #    print(word)
        kodet_tekst = caesar.encode(tekst)

    elif (cipher_to_use == "2"):
        n = int(input("Write your key (n): "))
        #tekst = tekst.split()
        #for word in tekst:
        #    print(word)
        kodet_tekst += Cipher.Multiplicative(n).encode(tekst)

    elif (cipher_to_use == "3"):
        n = input("Write your keys sperated by space (a n): ")
        kodet_tekst += Cipher.Affine((int(n[0]), int(n[2]))).encode(tekst)

    elif (cipher_to_use == "4"):
        n = input("Write your keyword: ")
        kodet_tekst += Cipher.Unbrakable(n).encode(tekst)

    else:
        print("You wrote somthin wrong")
        pass
    print(kodet_tekst)

    hacker = Person.Hacker(kodet_tekst).operate_cipher()

    """hacker1 = Hacker.Hacker(kodet_tekst).caesar_hack()
    hacker2 = Hacker.Hacker(kodet_tekst).multiplicative_hack()
    hacker3 = Hacker.Hacker(kodet_tekst).affine_hack()
    hacker4 = Hacker.Hacker(kodet_tekst).unbrakable_hacker()



    test = Cipher.Caesar(3)
    test2 = Cipher.Multiplicative(3)
    test3 = Cipher.Affine((3,2))
    test4 = Cipher.Unbrakable("zoo")
    test5 = Cipher.RSA(generate_koding_keys())

    encode = test.encode("zig")
    decode = test.decode(encode)
    encode2 = test2.encode("KUKE")
    decode2 = test2.decode(encode2)
    encode3 = test3.encode("RUKE")
    decode3 = test3.decode(encode3)
    encode4 = test4.encode("zoroastrianism")
    decode4 = test4.decode(encode4)
    encode5 = test5.encode("HAKE")
    decode5 = test5.decode(encode5)



    print(encode, decode)
    print(encode2,decode2)
    print(encode3 , decode3)
    print(encode4, decode4)
    print(encode5, decode5)

    print(test.verify("HAGE"))
    print(test2.verify("BADE"))
    print(test3.verify("RUKE"))
    print(test4.verify("zoroastrianism"))
    print(test5.verify("HAKE"))


    print(generate_koding_keys())"""
