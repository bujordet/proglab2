
import Cipher


class main():
    test = Cipher.Caesar(3)
    test2 = Cipher.Multiplicative(3)
    encode = test.encode("HAGE")
    decode = test.decode(encode)
    encode2 = test2.encode("BADE")
    decode2 = test2.decode(encode2)
    print(encode)
    print(decode)
    print(encode2)
    print(decode2)
    print(test.verify("HAGE"))
    print(test2.verify("BADE"))
