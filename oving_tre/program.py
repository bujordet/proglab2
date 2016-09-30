import Cipher


class main():
    test = Cipher.Caesar(3)
    test2 = Cipher.Multiplicative(3)
    test3 = Cipher.Affine((3,2))
    test4 = Cipher.Unbrakable("RUKE")


    decode = test.decode(encode)
    decode2 = test2.decode(encode2)
    decode3 = test3.decode(encode3)
    decode4 = test4.decode(encode4)

    encode = test.encode("HAGE")
    encode2 = test2.encode("KUKE")
    encode3 = test3.encode("RUKE")
    encode4 = test4.encode("PIZZATRYNE")

    print(encode, decode)
    print(encode2,decode2)
    print(encode3 , decode3)
    print(encode4, decode4)

    print(test.verify("HAGE"))
    print(test2.verify("BADE"))
    print(test3.verify("RUKE"))
    print(test4.verify("PIZZATRYNE"))
