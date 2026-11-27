# Koodikatselmoinnin raportti

Pyysin agenttia katselmoimaan `tennis_refactoring`-haaran muutokset suhteessa `main`-haaraan.

## Agentin tekemät huomiot

Agentin ensimmäinen ja ainoa varsinainen löydös koski diffissä ollutta `viikko4_varmuuskopio`-aliprojektiviitettä. Se ehdotti viitteen poistamista tai `.gitmodules`-tiedoston lisäämistä. Tämä huomio ei liittynyt tennisohjelman muutoksiin. Kun pyysin keskittymään tennis-koodiin, agentti totesi, ettei se löytänyt `tennis_game.py`:stä konkreettista toiminnallista virhettä. Se piti pisteiden tulostusta ja voiton ratkaisua tennislogiikan mukaisina ja nimien käyttöönottoa johdonmukaisena.

## Ehdotusten arviointi ja katselmoinnin hyödyllisyys

Aliprojektia koskeva ehdotus saattoi olla teknisesti perusteltu, jos aliprojekti olisi ollut tarkoituksellinen osa muutosta. Se oli kuitenkin tässä katselmoinnissa sivuseikka, eikä auttanut arvioimaan pyytämääni tennis-koodin refaktorointia. Tennis-koodiin ei tullut korjausehdotuksia.

Koin katselmoinnin hyödyllisyyden vähäiseksi. Toinen tarkistus voi vahvistaa luottamusta muutokseen, mutta tässä agentti ei perustellut arviotaan yksittäisillä testitapauksilla eikä ajanut testejä. Olisin hyötynyt tarkemmasta kommentista siitä, mitä pisteytyksen tilanteita se tarkisti.

Agentti ei huomannut sellaista varsinaista toiminnallista virhettä, jonka olisin itse jättänyt huomaamatta. Se jätti kuitenkin huomaamatta ylläpidettävyyteen liittyvän asian: `TennisGame`-luokan vakiot `LOVE`, `FIFTEEN`, `THIRTY` ja `DEUCE_SCORE` on määritelty mutta niitä ei käytetä. Ne voisi ottaa käyttöön pisteytyslogiikassa tai poistaa, jotta luokkaan ei jää harhaanjohtavia vakioita.

## Palaute ihmiseltä ja agentilta

Agentin kommentit tuntuivat vähemmän hyödyllisiltä kuin tiimikaverin palaute olisi tuntunut, koska huomio kohdistui aluksi pyytämäni koodimuutoksen ulkopuolelle. Tiimikaveri voisi kysyä tarkentavasti, kuuluuko kyseinen tiedosto katselmoinnin rajaukseen, ja keskustella löydöksen merkityksestä. Agentillekin kannattaa antaa selkeä rajaus, mutta katselmoijan vastuulla on lisäksi pitää palaute olennaisena.

Ihmisenä palautetta antaessa kannattaa olla asiallinen ja täsmällinen: osoittaa kohta, kertoa miksi sillä on merkitystä ja ehdottaa tarvittaessa korjausta. Kommentin tulisi kohdistua koodiin, ei sen tekijään. Epävarmuus kannattaa ilmaista kysymyksenä tai tarkistusehdotuksena, eikä pientä tyylihuomiota pidä esittää vakavana virheenä. Näin palautetta on helpompi ymmärtää ja käyttää.
