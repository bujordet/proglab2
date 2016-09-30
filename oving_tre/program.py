import Cipher
import crypto_utils
import random

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
    test = Cipher.Caesar(3)
    test2 = Cipher.Multiplicative(3)
    test3 = Cipher.Affine((3,2))
    test4 = Cipher.Unbrakable("RUKE")
    test5 = Cipher.RSA(generate_koding_keys())

    encode = test.encode("HAGE")
    decode = test.decode(encode)
    encode2 = test2.encode("KUKE")
    decode2 = test2.decode(encode2)
    encode3 = test3.encode("RUKE")
    decode3 = test3.decode(encode3)
    encode4 = test4.encode("PIZZATRYNE")
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
    print(test4.verify("PIZZATRYNE"))
    #print(test5.verify("HAKE"))


    print(generate_koding_keys())
