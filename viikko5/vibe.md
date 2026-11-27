# Vibe-koodauksen katselmointiraportti

Pyysin agenttia toteuttamaan `ohtuvarasto`-repositorion issuen 1. Yksinkertainen Flask-web-käyttöliittymä varastojen hallintaan.

## Päätyikö agentti toimivaan ja hyvään ratkaisuun

Kyllä. Ratkaisu täyttää issuen vaatimukset. Pääsivulla on lomake uuden varaston luontiin, lista varastoista saldoineen ja vapaine tiloineen, sekä erilliset lomakkeet tavaran lisäämiseen ja ottamiseen. Agentti käytti olemassa olevaa `Varasto`-luokkaa eikä kirjoittanut varastologiikkaa uudelleen. Kapasiteetin ylitys ja saldon yli menevä poisto estetään ennen kuin `Varasto`-luokan metodeja kutsutaan, joten käyttäjä saa selkeän virheilmoituksen.

Ratkaisu on tarkoituksellisen pieni. Varastot säilyvät muistissa, mikä vastaa issuen rajausta, jossa tietokantaa ei tarvita. Hyvänä yksityiskohtana agentti esti samannimisten varastojen luonnin, jotta valintalomakkeiden valinta ei jää epäselväksi.

## Miten varmistin, että ratkaisu toimii

Ajoin testit `varasto`-hakemistosta: `uv run coverage run --branch -m pytest -q` antoi 19 testiä, kaikki läpäisivät. `uv run coverage report -m` näytti `webapp.py`:n kattavuuden 100 %. Lisäksi tarkistin reitit komennolla `uv run flask --app webapp routes`; reitit `/`, `/varastot`, `/varastot/lisaa` ja `/varastot/ota` olivat olemassa oikeilla HTTP-metodeilla.

Ajoin myös Pylintin sekä koko repositorion juuritestauksessa että uusille tiedostoille projektin asetuksilla. Molemmat antoivat 10/10. Commitin yhteydessä pre-commitin pylint-hook läpäisi. Luin lopuksi diffin ja varmistin, että muutokset rajoittuvat web-käyttöliittymään, riippuvuuksiin, testeihin ja README:n käynnistysohjeisiin.

## Tekikö agentti testit ja olivatko ne hyviä

Kyllä. Testit ovat `varasto/src/tests/webapp_test.py` ja käyttävät Flaskin test clientiä. Ne kattavat varaston luonnin ja listauksen, lisäämisen, ottamisen, tilavuuden ylityksen, liian suuren poiston, virheellisen luvun, tyhjän nimen, saman nimen toistamisen sekä tuntemattoman varaston. Testit tarkistavat sekä käyttöliittymän tekstit että varaston todellisen saldon, joten ne eivät tyydy pelkkään HTTP-statuskoodiin.

Testit olivat hyviä ja olennaisia. Erityisesti virhetilanteiden testaus on tärkeää, koska `Varasto`-luokka itsessään leikkaa ylimenevät määrät hiljaa. Pieni miinus on se, että testit ovat HTML-merkkijonotestejä eivätkä todellista selaintestausta. Ulkoasun tai lomakkeiden visuaalisen toiminnan varsinainen varmistaminen jäi tekemättä. Tämä on kuitenkin perusteltua issuen rajauksessa, jossa ulkoasu on tarkoituksellisen yksinkertainen.

## Oliko koodi selkeää

Kyllä. `webapp.py` on jaettu pieniin funktioihin: `lue_luku` hoitaa syötteen jäsennyksen, `muotoile` näyttää luvut siististi, `ohjaa` flash-viestin ja uudelleenohjauksen, ja varsinaiset toiminnot `luo_varasto`, `lisaa_tavaraa` ja `ota_tavaraa` ovat erillään Flask-reiteistä. Funktion nimet kuvaavat toimintaa selkeästi.

## Opitko jotain uutta agentin tekemää koodia lukiessasi

Kyllä. Huomasin, että Flaskin `flash` vaatii `SECRET_KEY`-asetuksen myös ilman kirjautumista, koska viestit kulkevat session mukana.

Uutta oli myös se, että yksinkertainen `app.config`-sanakirja riittää tässä laajuudessa tilanhallintaan ilman tietokantaa.
