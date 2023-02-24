# Välityspalvelimen tuki NVDA:lle #

* Tekijä: Jose Manuel Delicado
* Yhteensopivuus: NVDA 2022.4 ja uudemmat
* Lataa [vakaa versio][1]

Tämän lisäosan avulla NVDA-ruudunlukija voi muodostaa yhteyden internetiin
yhden tai useamman välityspalvelimen kautta. Jotta tämä olisi mahdollista,
lisäosa tekee eri korjauksia Pythonin standardikirjastoon tai muokkaa
tiettyjä ympäristömuuttujia valitun kokoonpanon mukaan. Voit päivittää
NVDA:n ja sen lisäosat automaattisesti yritysympäristöstäsi ja jopa
suorittaa etäistuntoja, mikäli organisaatiosi välityspalvelin sallii sen.

## Ominaisuudet

* Tuki eri välityspalvelintyypeille: HTTP, SOCKS4 ja SOCKS5.
* Mahdollisuus ohjata kaikki tai vain tietty liikenne (HTTP, HTTPS, FTP)
  välityspalvelimen kautta.
* Mahdollisuus ohjata kaikki liikenne välityspalvelimen kautta ja sen
  jälkeen ohjata tietty liikenne muiden palvelimien kautta (sisäkkäiset
  välityspalvelimet).
* Tuki profiilin vaihtamiselle ja asetusten palauttamiselle: mikäli käytät
  yleensä NVDA:n massamuistiversiota, voit luoda useita profiileja eri
  ympäristöjä varten (koti, työ, toimisto1, toimisto2) ja ottaa ne käyttöön
  manuaalisesti.

## Käyttö

Tämä lisäosa lisää NVDA:n asetusvalintaikkunaan uuden
"Välityspalvelin"-kategorian. Tästä kategoriasta löydät neljä
asetusryhmää. Ensimmäisen avulla voit määrittää yleisen välityspalvelimen
kaikelle liikenteelle. Muiden ryhmien avulla voit määrittää
välityspalvelimet vain tietyille protokollille. Kaikissa ryhmissä on
seuraavat kentät:

* Isäntä: välityspalvelimen isäntänimi tai IP-osoite. Jätä tyhjäksi
  poistaaksesi kyseisen välityspalvelimen käytöstä.
* Portti: palvelimen portti.
* Käyttäjänimi: valinnainen. Käyttäjänimi palvelimen todennusta varten.
* Salasana: valinnainen. Salasana palvelimen todentamiseen. Huomaa, että
  salasanaa ei vaadita SOCKS4-palvelimille.

Edellisten kenttien lisäksi ensimmäisessä asetusryhmässä on käytettävissä
seuraavat vaihtoehdot:

* SOCKS-välityspalvelimen tyyppi: SOCKS4, SOCKS5 tai HTTP voidaan valita.
* Käytä välityspalvelinta DNS-pyyntöihin, jos mahdollista: kun tämä
  valintaruutu on valittuna, isäntä- tai toimialueen nimet lähetetään
  suoraan välityspalvelimen ratkaistavaksi. Kun valintaruutu ei ole
  valittuna, nimet ratkaistaan paikallisesti ja palvelin saa vain
  kohde-IP-osoitteen. Huomaa, että kaikki SOCKS4-välityspalvelimet eivät tue
  tätä vaihtoehtoa.

Useimpien käyttäjien on yleensä määritettävä vain ensimmäinen
asetusryhmä. Jos et tiedä välityspalvelimesi tietoja, kysy niitä
organisaatiosi verkonvalvojalta.

## Rajoitukset

* Erittäin rajoittunut IPv6-tuki.
* Kaikki välityspalvelimet eivät tue UDP-liikennettä.
* Ulkoiset DLL-kirjastot eivät noudata tässä lisäosassa määritettyjä
  asetuksia.
* HTTP-välityspalvelimille tuetaan vain
  perustodennusta. Tiivistelmätodennusta ei tueta.
* Jotta kaikki liikenne (HTTPS-yhteydet mukaan lukien) voidaan ohjata
  uudelleen HTTP-välityspalvelimen kautta, palvelimen on tuettava
  CONNECT-HTTP-menetelmää.
* "Suora yhteys" -tilaa ei voi määrittää. Jos poistat tietyn
  välityspalvelimen käytöstä, sen sijaan käytetään järjestelmän oletusarvoa.

## Muutosloki

### Versio 1.2

* Yhteensopiva NVDA 2023.1:n kanssa.
* Turvallisuussyistä NVDA:n vähimmäisversioksi on määritetty 2022.4.
* Käännöksiä päivitetty.

### Versio 1.1

* Yhteensopiva NVDA 2022.1:n kanssa.
* Turvallisuussyistä NVDA:n vähimmäisversioksi on asetettu 2021.3.
* Korjattu socket.getaddrinfo-funktio, kun "Käytä välityspalvelinta
  dns-pyyntöihin, jos mahdollista" -valintaruutu on valittuna ja yleinen
  välityspalvelin on määritetty.

### Versio 1.0

* Ensimmäinen versio.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=nvdaproxy
