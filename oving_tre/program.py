
import Cipher


class main():
    test = Cipher.Multiplicative(3)
    encode = test.encode("HAGE")
    decode = test.decode(encode)
    print(encode)
    print(decode)
    print(test.verify("HAGE"))
