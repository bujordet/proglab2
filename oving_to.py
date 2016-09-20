
import random
#import matplotlib.pyplot as plt

Stein = 0
Saks = 1
Papir = 2

__auther__ = 'Morten Bujordet'

class Spiller(object):
    """docstring for """
    def __init__(self, mode):
        self.mode = mode
        self.stein = 0
        self.saks = 0
        self.papir = 0
        self.poeng = 0
        self.seiere = 0

    def velg_aksjon(self):
        return random.randint(0,2)

    def motta_resultat(self, vinner, spiller2):
        #vinner: selv == 2, uavgjort == 1, taper == 0
        if (vinner == 2):
            self.poeng += 1
            self.seiere += 1
        elif (vinner == 1):
            self.poeng += 0.5
        return self.poeng

    def oppgi_navn(self):
        return self.navn

    def spill_mest_vanlig(self, mest):
        if(mest[0] == mest[1] == mest[2]):
            return random.randint(0,2)
        index = mest.index(max(mest))
        return super.velg_aksjon(index)

class Tilfeldig(Spiller):
    """docstring for random play"""
    def __init__(self):
        super().__init__("Tilfeldig")

    def velg_aksjon(self):
        return super.velg_aksjon()

    #super.motta_resultat
    #super.oppgi_navn

class Sekvensiell(Spiller):
    """docstring for sec. play"""
    aksjon = 0
    def __init__(self):
        super().__init__("Sekvensiell")

    def velg_aksjon(self):
        Sekvensiell.aksjon += 1
        if Sekvensiell.aksjon > 2:
            Sekvensiell.aksjon = 0
        return Sekvensiell.aksjon

    #super.motta_resultat
    #super.oppgi_navn

class MestVanlig(Spiller):
    def __init__(self):
        super().__init__("MestVanlig")
        self.mest = [0,0,0] #index: 0 = stein, 1 = saks, 2 = papir

    def velg_aksjon(self):
        super.spill_mest_vanlig(self.mest)

    def motta_resultat(self, motstanderResultat):
        self.mest[motstanderResultat] += 1



class Historiker(Spiller):
    """docstring for """
    def __init__(self, husk):
        super().__init__("Historiker")
        self.husk = husk
        self.tidligere = []
        self.sequence = []
        self.mest = [0,0,0]

    def velg_aksjon(self):
        if (len(self.tidligere) <= self.husk):
            return super.velg_aksjon()
        self.sequence = self.tidligere[-(self.husk):]
        for e in self.tidligere:
            if (self.tidligere[e: e+self.husk] == self.sequence):
                self.mest[e + self.husk +1] += 1
        super.spill_mest_vanlig(self.mest)



    def motta_resultat(self, motstanderResultat):
        super.motta_resultat()
        self.sequence.append(motstanderResultat)

class EnkeltSpill(Spiller):
    """docstring for """
    def __init__(self, spiller1, spiller2):
        #super().__init__("EnkeltSpill")
        self.spiller1 = spiller1
        self.spiller2 = spiller2
        self.vinner = -1


    def gjennomfoer_spill(self):
        spiller_en = self.spiller1.velg_aksjon()
        spiller_to = self.spiller2.velg_aksjon()
        vinner = finn_vinner(spiller_en, spiller_to)
        if (vinner == 0):
            self.spiller2.motta_resultat(2, self.spiller1)
            self.spiller1.motta_resultat(0, self.spiller2)
            self.vinner = self.spiller2
        elif (vinner == 1):
            self.spiller2.motta_resultat(1, self.spiller1)
            self.spiller1.motta_resultat(1, self.spiller2)
            self.vinner = None
        else:
            self.spiller1.motta_resultat(2, self.spiller2)
            self.spiller2.motta_resultat(0, self.spiller1)
            self.vinner = self.spiller1

    def __str__(self, resultat):
        if (self.vinner == None):
            return "Det er ingen vinner"
        elif (self.vinner == -1):
            return "Det er ikke spilt enda"
        else:
            return "Vinneren ble " + self.vinner.__str__()


    def finn_vinner(self, spiller1, spiller2):
        if (spiller1 == spiller2):
            poeng = 1
        elif (spiller1 == 0 and spiller2 == 1 or spiller1 == 1 and spiller2 == 2 or spiller1 == 2 and spiller2 == 0):
            poeng = 2
        else:
            poeng = 0
        return poeng

class MangeSpill(object):
    """docstring for """
    def __init__(self, spiller1, spiller2, antall_spill):
        #super().__init__("MangeSpill")
        self.spiller1 = spiller1
        self.spiller2 = spiller2
        self.antall_spill = antall_spill
        self.plotX = []
        self.plotY = []

    def arranger_enkeltspill():
        spill = EnkeltSpill(self.spiller1, self.spiller2)
        spiller_en, spiller_en, vinner = spill.gjennomfoer_spill()
        print(self.spiller1.oppgi_navn() + ":", spiller_en.oppgi_navn()+".",self.spiller2.oppgi_navn() + ":", spiller_to.oppgi_navn()+".", "Vinneren".oppgi_navn())


    def arranger_turnering(self):
        for i in range(self.antall_spill):
            self.arranger_enkeltspill()
            self.plotY.append(self.spiller2.seiere/i+1)
            self.plotX.append(i+1)
        print("Turneringen er ferdig!", self.spiller1.oppgi_navn(), "vant", self.spiller1.poeng, "ganger.", self.spiller2.oppgi_navn(), "vant", self.spiller2.poeng, "ganger")
        print(self.spiller1.oppgi_navn() + " vant " + str(((self.spiller1.poeng/float(self.antall_spill))*100))+"% av gangene.")
        print(self.spiller2.oppgi_navn() + " vant " + str(((self.spiller2.poeng/float(self.antall_spill))*100))+"% av gangene.")

    ''''def plot(self, plotX, plotY):
        plt.plot(plotX, plotY)
        plt.ylabel("Vinnerprosent")
        plt.xlabel("Antall kamper")
        plt.axes([0, self.antall_spill, 0, 1])
        plt.show()
'''
class main():
    spiller1 = Historiker(2)
    spiller2 = Tilfeldig()
    spiller3 = MestVanlig()
    Spiller4 = Sekvensiell()
    mangeSpill = MangeSpill(spiller2, spiller3, 100)
