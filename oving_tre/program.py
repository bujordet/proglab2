import Cipher


class main():
    test = Cipher.Caesar(3)
    test2 = Cipher.Multiplicative(3)
    test3 = Cipher.Affine((3,2))
    test4 = Cipher.Unbrakable("RUKE")

    encode = test.encode("HAGE")
    decode = test.decode(encode)
    encode2 = test2.encode("KUKE")
    decode2 = test2.decode(encode2)
    encode3 = test3.encode("RUKE")
    decode3 = test3.decode(encode3)
    encode4 = test4.encode("PIZZATRYNE")
    decode4 = test4.decode(encode4)


    print(encode, decode)
    print(encode2,decode2)
    print(encode3 , decode3)
    print(encode4, decode4)

    print(test.verify("HAGE"))
    print(test2.verify("BADE"))
    print(test3.verify("RUKE"))
    print(test4.verify("PIZZATRYNE"))
