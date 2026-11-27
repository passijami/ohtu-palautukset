# Vibe-koodauksen katselmointiraportti

Pyysin agenttia toteuttamaan `ohtuvarasto`-repositorion issuen 1: yksinkertaisen Flask-web-käyttöliittymän varastojen hallintaan. Agentti teki muutokset `web-ui`-haaraan ja commitoi ne tunnisteella `3061f85`.

## Päätyikö agentti toimivaan ja hyvään ratkaisuun

Kyllä. Ratkaisu täyttää issuen vaatimukset: pääsivulla on lomake uuden varaston luontiin, lista varastoista saldoineen ja vapaine tiloineen, sekä erilliset lomakkeet tavaran lisäämiseen ja ottamiseen. Agentti käytti olemassa olevaa `Varasto`-luokkaa eikä kirjoittanut varastologiikkaa uudelleen. Kapasiteetin ylitys ja saldon yli menevä poisto estetään ennen kuin `Varasto`-luokan metodeja kutsutaan, joten käyttäjä saa selkeän virheilmoituksen sen sijaan että määrä hiljaa leikkaantuisi.

Ratkaisu on tarkoituksellisen pieni. Varastot säilyvät muistissa `app.config["VARASTOT"]`-sanakirjassa, mikä vastaa issuen rajausta, jossa tietokantaa ei tarvita. Hyvänä yksityiskohtana agentti esti samannimisten varastojen luonnin, jotta valintalomakkeiden valinta ei jää epäselväksi.

## Miten varmistin, että ratkaisu toimii

Ajoin testit `varasto`-hakemistosta: `uv run coverage run --branch -m pytest -q` antoi 19 testiä, kaikki läpäisivät. `uv run coverage report -m` näytti `webapp.py`:n kattavuuden 100 %. Lisäksi tarkistin reitit komennolla `uv run flask --app webapp routes`; reitit `/`, `/varastot`, `/varastot/lisaa` ja `/varastot/ota` olivat olemassa oikeilla HTTP-metodeilla.

Ajoin myös Pylintin sekä koko repositorion juuritestauksessa että uusille tiedostoille projektin asetuksilla; molemmat antoivat 10/10. Commitin yhteydessä pre-commitin pylint-hook läpäisi. Luin lopuksi diffin ja varmistin, että muutokset rajoittuvat web-käyttöliittymään, riippuvuuksiin, testeihin ja README:n käynnistysohjeisiin.

## Tekikö agentti testit, ja olivatko ne hyviä

Kyllä. Testit ovat `varasto/src/tests/webapp_test.py` ja käyttävät Flaskin test clientiä. Ne kattavat varaston luonnin ja listauksen, lisäämisen, ottamisen, tilavuuden ylityksen, liian suuren poiston, virheellisen luvun, tyhjän nimen, saman nimen toistamisen sekä tuntemattoman varaston. Testit tarkistavat sekä käyttöliittymän tekstit että varaston todellisen saldon, joten ne eivät tyydy pelkkään HTTP-statuskoodiin.

Testit olivat hyviä ja olennaisia. Erityisesti virhetilanteiden testaus on tärkeää, koska `Varasto`-luokka itsessään leikkaa ylimenevät määrät hiljaa. Pieni miinus on se, että testit ovat HTML-merkkijonotestejä eivätkä todellista selaintestausta; ulkoasun tai lomakkeiden visuaalisen toiminnan varsinainen varmistaminen jäi tekemättä. Tämä on kuitenkin perusteltua issuen rajauksessa, jossa ulkoasu on tarkoituksellisen yksinkertainen.

## Oliko koodi selkeää

Kyllä. `webapp.py` on jaettu pieniin funktioihin: `lue_luku` hoitaa syötteen jäsennyksen, `muotoile` näyttää luvut siististi, `ohjaa` flash-viestin ja uudelleenohjauksen, ja varsinaiset toiminnot `luo_varasto`, `lisaa_tavaraa` ja `ota_tavaraa` ovat erillään Flask-reiteistä. Funktion nimet ovat suomeksi ja kuvaavat toimintaa hyvin. Myös Jinja-pohja on suoraviivainen: flash-viestit, varastolista ja kolme lomaketta ovat omissa `section`-elementeissään.

Reittifunktioiden `_route`-pääte on hieman kankea, mutta se selkeyttää eron käyttöliittymäkutsun ja liiketoimintafunktion välillä. Muuten koodi noudattaa hyvin projektin tyyliä ja Pylintin rajoituksia.

## Opitko jotain uutta agentin tekemää koodia lukiessasi

Kyllä. Huomasin, että Flaskin `flash` vaatii `SECRET_KEY`-asetuksen myös ilman kirjautumista, koska viestit kulkevat session mukana. Lisäksi testit paljastivat, että Jinja escapee apostrofit HTML-muotoon `&#39;`; testeissä piti käyttää `html.unescape`, jotta flash-viestien tekstiä voitiin verrata suomeksi.

Uutta oli myös se, että yksinkertainen `app.config`-sanakirja riittää tässä laajuudessa tilanhallintaan ilman tietokantaa, ja että desimaalipilkku voidaan hyväksyä helposti korvaamalla se pisteellä ennen `float`-muunnosta. Lisäksi opin käytännön syystä, että pre-commitin järjestelmä-Pylint tarvitsee Flaskin myös juuriprojektin ympäristössä, vaikka sovellus itsessään asennetaan `varasto`-projektiin.
