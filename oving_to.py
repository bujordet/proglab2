
import random
import matplotlib.pyplot as plt
from collections import Counter

Stein = 0
Saks = 1
Papir = 2

__auther__ = 'Morten Bujordet'

class Spiller(object):
    """docstring for """
    def __init__(self):
        #self.mode = mode
        self.stein = 0
        self.saks = 0
        self.papir = 0
        self.poeng = 0
        self.seiere = 0
        self.sequence = []

    def velg_aksjon(self):
        return random.randint(0,2)

    def motta_resultat(self, vinner, other_trekk):
        #vinner: selv == 2, uavgjort == 1, taper == 0
        if (vinner == 2):
            self.poeng += 1
            self.seiere += 1
        elif (vinner == 1):
            self.poeng += 0.5
        self.sequence.append(other_trekk)
        return self.poeng

    def oppgi_navn(self):
        return self.__class__.__name__


class Tilfeldig(Spiller):
    """docstring for random play"""


    #super.motta_resultat
    #super.oppgi_navn

class Sekvensiell(Spiller):
    """docstring for sec. play"""
    aksjon = 0

    def velg_aksjon(self):
        Sekvensiell.aksjon += 1
        if Sekvensiell.aksjon > 2:
            Sekvensiell.aksjon = 0
        return Sekvensiell.aksjon

    #super.motta_resultat
    #super.oppgi_navn

class MestVanlig(Spiller):

    #def __init__(self):
     #   super().__init__("MestVanlig")
      #  #self.mest = [0,0,0] #index: 0 = stein, 1 = saks, 2 = papir

    def velg_aksjon(self):
        if(not self.sequence):
            return super().velg_aksjon()
        print("siste: "+ str(self.sequence[-1]))
        #index = self.mest.index(max(self.mest))
        return Counter(self.sequence).most_common(1)[0][0]

    #def motta_resultat(self, vinner, motstanderResultat):
    #    print(motstanderResultat)
    #    super().motta_resultat(vinner, motstanderResultat)
    #    self.mest[motstanderResultat] += 1



class Historiker(Spiller):
    """docstring for """
    def __init__(self, husk):
        super().__init__()
        self.husk = husk
        self.bit = []
        self.mest = []


    def velg_aksjon(self):
        if (len(self.sequence) <= self.husk):
            return super().velg_aksjon()
        self.bit = self.sequence[-(self.husk):]
        for e in self.sequence:
            if (self.sequence[e: e+self.husk] == self.bit):
                self.mest.append(e + self.husk)

        if (not self.mest):
            return super().velg_aksjon()
        return Counter(self.mest).most_common(1)[0][0]
        #if(self.mest[0] == self.mest[1] == self.mest[2]):
        #    return random.randint(0,2)
        #index = self.mest.index(max(self.mest))
        #return super().velg_aksjon(index)



    def motta_resultat(self,vinner, motstanderResultat):
        super().motta_resultat(vinner, motstanderResultat)
        self.sequence.append(motstanderResultat)

class EnkeltSpill(Spiller):
    """docstring for """
    def __init__(self, spiller1, spiller2):
        #super().__init__("EnkeltSpill")
        self.spiller1 = spiller1
        self.spiller2 = spiller2
        self.vinner = -1

    def finn_vinner(self, spiller1, spiller2):
        if (spiller1 == spiller2):
            poeng = 1
        elif (spiller1 == 0 and spiller2 == 1 or spiller1 == 1 and spiller2 == 2 or spiller1 == 2 and spiller2 == 0):
            poeng = 2
        else:
            poeng = 0
        return poeng



    def gjennomfoer_spill(self):
        spiller_en = self.spiller1.velg_aksjon()
        spiller_to = self.spiller2.velg_aksjon()
        vinner = self.finn_vinner(spiller_en, spiller_to)
        if (vinner == 0):
            self.spiller2.motta_resultat(2, spiller_en)
            self.spiller1.motta_resultat(0, spiller_to)
            self.vinner = self.spiller2
        elif (vinner == 1):
            self.spiller2.motta_resultat(1, spiller_en)
            self.spiller1.motta_resultat(1, spiller_to)
            self.vinner = None
        else:
            self.spiller1.motta_resultat(2, spiller_to)
            self.spiller2.motta_resultat(0, spiller_en)
            self.vinner = self.spiller1
        return self.spiller1, self.spiller2, self.vinner
    def __str__(self, resultat):
        if (self.vinner == None):
            return "Det er ingen vinner"
        elif (self.vinner == -1):
            return "Det er ikke spilt enda"
        else:
            return "Vinneren ble " + self.vinner.__str__()



class MangeSpill(object):
    """docstring for """
    def __init__(self, spiller1, spiller2, antall_spill):
        #super().__init__("MangeSpill")
        self.spiller1 = spiller1
        self.spiller2 = spiller2
        self.antall_spill = antall_spill
        self.plotX = []
        self.plotY = []

    def arranger_enkeltspill(self):
        spill = EnkeltSpill(self.spiller1, self.spiller2)
        spiller_en, spiller_to, vinner = spill.gjennomfoer_spill()
        print(self.spiller1.oppgi_navn() + ":", spiller_en.oppgi_navn()+".",self.spiller2.oppgi_navn() + ":", spiller_to.oppgi_navn()+".", "Vinneren".__str__())


    def arranger_turnering(self):
        for i in range(self.antall_spill):
            self.arranger_enkeltspill()
            self.plotY.append(self.spiller2.seiere/(i+1))
            self.plotX.append(i+1)
        print("Turneringen er ferdig!", self.spiller1.oppgi_navn(), "vant", self.spiller1.poeng, "ganger.", self.spiller2.oppgi_navn(), "vant", self.spiller2.poeng, "ganger")
        print(self.spiller1.oppgi_navn() + " vant " + str(((self.spiller1.poeng/float(self.antall_spill))*100))+"% av gangene.")
        print(self.spiller2.oppgi_navn() + " vant " + str(((self.spiller2.poeng/float(self.antall_spill))*100))+"% av gangene.")

    def plot(self, plotX, plotY):
        plt.plot(plotX, plotY)
        plt.ylabel("Vinnerprosent")
        plt.xlabel("Antall kamper")
        plt.axes([0, self.antall_spill, 0, 1])
        plt.show()

class main():
    spiller1 = Historiker(2)
    spiller2 = Tilfeldig()
    spiller3 = MestVanlig()
    spiller4 = Sekvensiell()
    mangeSpill = MangeSpill(spiller1, spiller4, 200)
    #enkeltSpill = MangeSpill.arranger_enkeltspill()
    mangeSpill.arranger_turnering()
    mangeSpill.plot(mangeSpill.plotX, mangeSpill.plotY)
