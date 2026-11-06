# Kokemuksia OpenCode-agentin käytöstä

## `top_goal_scorers`-metodi

Metodi toteutettiin docstringin mukaisesti: se järjestää pelaajat maalien
mukaan laskevaan järjestykseen ja palauttaa viipaloimalla enintään
`how_many` pelaajaa. Toteutus käyttää `PlayerStats`-luokan olemassa olevaa
`self.players`-listaa. Järjestämistapa on samankaltainen kuin luokan muissa
metodeissa, vaikka `sorted`-funktiolla tehty toteutus poikkeaa hieman
`top_by_nationality`- ja `top_by_team`-metodien listan keräämisestä ja
`sort`-kutsusta.

## Pylintin varoitukset

Agentin selitys piti pääosin paikkansa. Pylint ei ilmoittanut ohjelman
suoritusvirheistä, vaan staattisen tarkistuksen huomautuksia: puuttuvia
docstringejä, liian pitkän rivin, käyttämättömän tuonnin, puuttuvan
HTTP-pyynnön aikakatkaisun ja väärän tuontijärjestyksen. Lisäksi se huomautti,
että `Player`- ja `PlayerReader`-luokissa on vähän julkisia metodeja. Tämä oli
luokkien nykyisen tehtävän kannalta tarkoituksellista. Pylintin kuvaus näistä
huomautuksista oli oikea; kyse ei ollut varsinaisista ohjelman ajonaikaisista
virheistä.

## Ratkaisu ja testit

Agentti toteutti myös joukkueen pelaajien hakemisen pistejärjestyksessä.
`PlayerStats.top_by_team` suodattaa joukkueen pelaajat ja järjestää heidät
maalien ja syöttöjen summan mukaan. Käyttöliittymässä voi valita haun
kansalaisuuden tai joukkueen mukaan.

`PlayerStats`-luokalle tehtiin neljä `unittest`-testiä. Ne testaavat
kansalaisuuden ja joukkueen mukaan suodatusta sekä pistejärjestystä,
maalintekijöiden järjestystä ja tulosmäärän rajaamista. Testeissä käytetään
`PlayerReaderStub`-luokkaa, joka palauttaa testidatan suoraan. Oikeaa
`PlayerReader`-luokkaa ei käynnistetä, joten testit eivät käytä verkkoyhteyttä.
Kaikki neljä testiä läpäisivät.

Testien perusidea on sama kuin edellisellä viikolla: `unittest`, stub-lukija,
`setUp` ja tulosten tarkistaminen `assertEqual`-kutsuilla. Rakenteessa on
kuitenkin eroja. Edellisen viikon testissä lisättiin `src`-hakemisto Pythonin
hakupolkuun `sys.path`-muutoksella, kun taas tällä viikolla testit ajettiin
`PYTHONPATH=src`-ympäristömuuttujalla. Lisäksi tämän viikon `Player` ottaa
vastaan sanakirjan eikä erillisiä konstruktoriargumentteja, joten testidatan
luonti on sen mukaista.

## Pylint ja opit

Alkuperäisessä Pylint-ajossa löytyi tyyli- ja dokumentointihuomautuksia.
Korjausten jälkeen `uv run pylint src` antoi tulokseksi 10/10. Testejä
tarkistettaessa Pylint löysi myös testitiedostosta aluksi puuttuvia
docstringejä ja importtiasetukseen liittyviä huomautuksia. Testit ajettiin
uudelleen ja Pylintille annettiin `src`-hakemisto hakupolulle; tällöin myös
`src`- ja `tests`-tiedostojen yhteinen ajo antoi 10/10.

Opin, että pieni stub tekee riippuvuuden korvaamisesta suoraviivaista ja
pitää yksikkötestit erillään verkkopalvelusta. Opin myös, että Pylintin
arvosana kattaa dokumentoinnin ja rakenteen kaltaisia asioita, ei vain sitä,
toimiiko koodi. Testien ja Pylintin ajotapa kannattaa sovittaa projektin
hakemistorakenteeseen: tässä `src`-hakemiston moduulit täytyi lisätä
Pythonin tuontipolulle testejä ajettaessa.
