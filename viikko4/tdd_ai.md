# Reflektio TDD-harjoituksesta ja AI-agentin käytöstä

Agentti päätyi mielestäni hyvään ja selkeään toteutukseen. Ostoskorin toiminnot,
kuten tuotteiden lisääminen ja poistaminen, hinnan laskeminen, korin
tyhjentäminen sekä ostosten ryhmittely tuotteen nimen perusteella on toteutettu
ymmärrettävästi. Testit kattavat näiden toimintojen keskeiset tapaukset esim. yhden
ja useamman tuotteen lisäämisen, saman tuotteen toistumisen, poistamisen ja korin
tyhjentämisen. Testien nimet kuvaavat hyvin tarkistettavaa toimintaa, joten
kokonaisuutta on helppo lukea.

Osassa A agentti pysyi minimitoteutuksessa. Se teki vain toiminnan vaatiman
ratkaisun eikä lisännyt tarpeetonta rakennetta. Testejä ei muokattu
toteutuksen läpäisemiseksi.

En huomannut agentin yrittäneen huijata tai kovakoodata yksittäisten testien
odottamia tuloksia. Toteutus perustuu syötettyihin tuotteisiin ja niiden
ominaisuuksiin, eikä esim. palauteta testien odottamia kiinteitä
lukumääriä tai hintoja. Tarkistin kuitenkin lopputuloksen itse, mikä on tärkeää
myös silloin, kun agentin tekemä koodi vaikuttaa siistiltä.

Työnjaoista A tuntui minusta paremmalta. Testien tekeminen itse loi
luotettavuuden tunnetta, koska sain itse määritellä, millaista toimintaa
toteutukselta odotetaan. Opencoden tekemä koodi oli kunnollista ja siistiä, ja
sen avulla työ valmistui nopeammin. Nopeusero ei kuitenkaan ollut huomattava,
sillä tekoälyn tuottama koodi täytyi joka tapauksessa tarkastaa itse. Testien
kirjoittaminen itse tuntui siksi varmemmalta tavalta hyödyntää agenttia
toteutuksen apuna.
