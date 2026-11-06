# Kokemuksia OpenCode

## `top_goal_scorers`-metodi

OpenCode toteutti metodin docstringin mukaisesti. Metodi järjestää pelaajat tehtyjen maalien mukaan suurimmasta pienimpään ja palauttaa enintään `how_many` pelaajaa. Toteutuksessa hyödynnetään `PlayerStats`-luokan olemassa olevaa `self.players`-listaa.

Toteutus sopii pääosin luokan muuhun koodityyliin. Pieni ero muihin metodeihin on siinä, että tässä käytetään `sorted`-funktiota, kun taas esimerkiksi `top_by_nationality`- ja `top_by_team`-metodeissa pelaajia kerätään listaan ja lista järjestetään erillisellä `sort`-kutsulla.

## Pylintin varoitukset

Agentin selitys Pylintin varoituksista piti pääosin paikkansa. Kyse ei ollut ohjelman varsinaisista suoritusvirheistä, vaan koodin tyyliin ja rakenteeseen liittyvistä huomautuksista. Pylint ilmoitti esimerkiksi puuttuvista docstringeistä, liian pitkästä rivistä, käyttämättömästä tuonnista, HTTP-pyynnöstä puuttuvasta aikakatkaisusta ja importtien väärästä järjestyksestä.

Lisäksi Pylint huomautti, että `Player`- ja `PlayerReader`-luokissa on vähän julkisia metodeja. Tämä ei kuitenkaan ollut tässä tapauksessa ongelma, sillä luokkien tehtävät ovat melko rajattuja. Agentti osasi selittää, mistä huomautukset johtuivat ja miksi niihin kannattaa kiinnittää huomiota. Kyse ei siis ollut varsinaisista ajonaikaisista virheistä.

## Ratkaisu ja testit

Agentti onnistui toteuttamaan myös uuden toiminnallisuuden, jolla voidaan näyttää valitun joukkueen pelaajat pisteiden mukaan järjestettynä. `PlayerStats.top_by_team` hakee ensin valitun joukkueen pelaajat ja järjestää heidät tehtyjen maalien ja syöttöjen yhteismäärän perusteella. Myös käyttöliittymään lisättiin mahdollisuus valita, haetaanko pelaajia kansalaisuuden vai joukkueen mukaan.

`PlayerStats`-luokalle tehtiin neljä `unittest`-testiä. Niillä testataan pelaajien suodattamista kansalaisuuden ja joukkueen perusteella, pistejärjestystä sekä maalintekijöiden järjestämistä ja tulosten määrän rajaamista.

Testeissä käytettiin `PlayerReaderStub`-luokkaa, joka palauttaa valmiiksi määriteltyä testidataa. Näin oikeaa `PlayerReader`-luokkaa ei tarvinnut käyttää, eikä testeissä tehty verkkopyyntöjä. Kaikki neljä testiä menivät läpi.

Testien tekeminen oli perusidealtaan samanlaista kuin edellisellä viikolla. Käytössä olivat edelleen `unittest`, stub-luokka, `setUp` ja tulosten tarkistaminen `assertEqual`-kutsuilla. Toteutuksessa oli kuitenkin muutamia eroja. Edellisellä viikolla `src`-hakemisto lisättiin Pythonin hakupolulle `sys.path`-muutoksella, kun taas tällä viikolla testit ajettiin `PYTHONPATH=src`-ympäristömuuttujan avulla. Lisäksi tämän viikon `Player`-luokka ottaa vastaan sanakirjan erillisten konstruktoriargumenttien sijaan, joten myös testidatan luominen oli hieman erilaista.

## Pylint ja opit

Aluksi Pylint löysi koodista useita tyyliin ja dokumentointiin liittyviä huomautuksia. Korjausten jälkeen `uv run pylint src` antoi tulokseksi 10/10. Myös testitiedostoa tarkistettaessa Pylint löysi aluksi puuttuvia docstringejä ja huomautettavaa importtien järjestyksestä. Kun nämä korjattiin ja `src`-hakemisto lisättiin Pythonin hakupolulle, myös `src`- ja `tests`-hakemistojen yhteinen tarkistus meni läpi arvosanalla 10/10.

Tehtävän aikana opin erityisesti, miten stubin avulla voidaan korvata ohjelman riippuvuus toisesta luokasta. Näin yksikkötestit pysyvät itsenäisinä eivätkä ole riippuvaisia verkkopalvelun toiminnasta. Opin myös, että Pylint tarkistaa koodista paljon muutakin kuin sen, toimiiko ohjelma. Se kiinnittää huomiota esimerkiksi dokumentointiin, koodin rakenteeseen ja yhtenäiseen tyyliin.

Lisäksi huomasin, että testien suorittamisessa kannattaa huomioida projektin hakemistorakenne ja Pythonin moduulien tuontipolut. Tässä projektissa `src`-hakemisto piti saada Pythonin hakupolulle, jotta testit löysivät tarvittavat moduulit. OpenCoden käytöstä jäi myös kokemus siitä, että agentti pystyy nopeuttamaan toteutusta, mutta sen tekemät muutokset pitää silti lukea ja testata itse ennen hyväksymistä.
