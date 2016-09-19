
import random

Stein = 0
Saks = 1
Papir = 2


class Spiller(object):
    """docstring for """
    def __init__(self, navn):
        self.navn = navn
        self.stein = 0
        self.saks = 0
        self.papir = 0

    def velg_aksjon(self):
        return aksjon

    def motta_resultat(self, spiller2):

        return poeng

    def oppgi_navn(self):
        return self.navn

class Tilfeldig(Spiller):
    """docstring for random play"""
    def __init__(self):
        super(, self).__init__("Tilfeldig")

    def velg_aksjon(self):
        aksjon = random.randint(0,2)
        return aksjon

    #super.motta_resultat
    #super.oppgi_navn

class Sekvensiell(Spiller):
    """docstring for sec. play"""
    aksjon = 0
    def __init__(self):
        super(, self).__init__("Sekvensiell")

    def velg_aksjon(self):
        Sekvensiell.aksjon += 1
        if Sekvensiell.aksjon > 2:
            Sekvensiell.aksjon = 0
        return Sekvensiell.aksjon

    #super.motta_resultat
    #super.oppgi_navn

class MestVanlig(Spiller):
    def __init__(self):
        super(,self).__init__("MestVanlig")
        self.mest = [0,0,0] #index: 0 = stein, 1 = saks, 2 = papir

    def velg_aksjon(self):
        if(self.mest[0] == self.mest[1] == self.mest[2]):
            return random.randint(0,2)
        index = self.mest.index(max(self.mest))
        return super.velg_aksjon(index)

    def motta_resultat(self, motstanderResultat):
        self.mest[motstanderResultat] += 1



class Historiker(Spiller):
    """docstring for """
    def __init__(self, husk):
        super(, self).__init__("Historiker")
        self.husk = husk
        self.sequence = []

    def velg_aksjon(self):

    def motta_resultat(self, motstanderResultat):
        super.

class EnkeltSpill(Spiller):
    """docstring for """
    def __init__(self, spill):
        super(, self).__init__("EnkeltSpill")
        self.spill = spill

    def finn_vinner(self, spiller1, spiller2):
        if (spiller1 == spiller2):
            poeng = 0
        elif (spiller1 == 0 and spiller2 == 1 or spiller1 == 1 and spiller2 == 2 or spiller1 == 2 and spiller2 == 0):
            poeng = 1
        else:
            poeng = 2
        return vinner
