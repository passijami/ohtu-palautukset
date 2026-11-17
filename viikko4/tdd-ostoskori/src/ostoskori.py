from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._tuotteet = []

    def tavaroita_korissa(self):
        return len(self._tuotteet)

    def hinta(self):
        return sum(tuote.hinta() for tuote in self._tuotteet)

    def lisaa_tuote(self, lisattava: Tuote):
        self._tuotteet.append(lisattava)

    def poista_tuote(self, poistettava: Tuote):
        pass

    def tyhjenna(self):
        pass

    def ostokset(self):
        ostokset = []
        for tuote in self._tuotteet:
            ostos = next((ostos for ostos in ostokset
                          if ostos.tuotteen_nimi() == tuote.nimi()), None)
            if ostos is None:
                ostokset.append(Ostos(tuote))
            else:
                ostos.muuta_lukumaaraa(1)
        return ostokset
