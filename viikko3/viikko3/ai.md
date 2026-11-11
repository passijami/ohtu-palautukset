# Kokemuksia tekoälyn käytöstä

Hyödynsin OpenCodea login-tehtävän koodin ja testien muokkaamisessa. Tekoälystä oli apua muutosten ideoinnissa, mutta sen ehdottama koodi ei kaikilta osin vastannut tehtävän vaatimuksia.

## Ohjetiedosto

OpenCode generoi projektille AGENTS.md-ohjetiedoston, jossa kerrottiin projektin rakenteesta ja kehitysympäristöstä. Jouduin tarkistamaan ja täydentämään ohjetiedostoa, jotta siinä kerrottiin selkeästi, että kyseessä on uv-projekti, miten sovellus käynnistetään, missä portissa se toimii, miten Robot Framework -testit suoritetaan ja missä käyttäjätunnuksen sekä salasanan validointi tapahtuu.

## Testit ennen toteutusta

Agentti noudatti pyyntöä kirjoittaa testit ennen toiminnallisuuden toteuttamista. Pyysin sitä tekemään ensin Robot Framework -testit ja varmistamaan, että ne epäonnistuvat ennen toteutuksen muuttamista. Tämän jälkeen agentti toteutti vaaditut toiminnallisuudet.

## Agentin ohjaaminen

Jouduin ohjaamaan agenttia jonkin verran matkan varrella. Tarkistin sen tekemiä muutoksia git diff -komennolla ja huomasin, että se oli muuttanut myös kirjautumiseen liittyvää login.robot-tiedostoa, vaikka tehtävä koski rekisteröitymistä. Lisäksi jouduin tarkistamaan testien odotuksia ja korjaamaan ylimääräisiä muutoksia. Agentin tuottamaa koodia ei siis voinut hyväksyä tarkistamatta.

## Mitä opin?

Opin käyttämään OpenCodea ohjelmistokehityksen apuna sekä ymmärsin paremmin testivetoisen kehityksen merkityksen. Opin myös tarkistamaan tekoälyn tekemät muutokset git diff -komennolla.

Jouduin itse tarkistamaan ja muokkaamaan koodia, koska tekoäly lisäsi ylimääräistä koodia, joka ei kuulunut tehtävän määrittelyyn.

Kokemus muistutti, että tekoälyn tuottamat muutokset pitää lukea ja arvioida huolellisesti eikä niitä kannata hyväksyä sellaisinaan. Vastuu on aina käyttäjällä.
