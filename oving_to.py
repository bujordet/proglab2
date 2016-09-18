

public class Spiller(object):
    """docstring for """
    def __init__(self, arg):
        super(, self).__init__()
        self.arg = arg

    def velg_aksjon():
        return aksjon

    def motta_resultat(spiller1, spiller2):

        print("Det ble spilt: " spiller1 "og " spiller2)
        bestem_vinner(finn_spiller(spiller1), finn_spiller(spiller2))


    def finn_spiller(spiller):
        if (spiller == "saks"):
            return 0
        elif (spiller == "papir"):
            return 1
        elif(spiller == "stein"):
            return 2
        else:
            return -1

    def bestem_vinner(num1, num2):
        if (num1 == num2):
            return "uavgjort"
        if (num1 == 0):
            
