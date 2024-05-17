# Podrška posrednika za NVDA (Proxy support for NVDA) #

* Autor: Jose Manuel Delicado
* NVDA kompatibilnost: 2023.3.4 i novije verzije
* Preuzmi [stabilnu verziju][1]

Ovaj dodatak omogućuje NVDA čitaču ekrana da se poveže s internetom putem
jednog ili više posredničkih poslužitelja. Da bi to bilo moguće, dodatak
primijenjuje razne zakrpe na standardnu Python biblioteku ili mijenja
određene varijable okruženja, ovisno o odabranoj konfiguraciji. Dodatak
omogućuje aktualiziranje NVDA čitača i njegovih dodataka u vlastitom
poslovnom okruženju, kao i izvođenje udaljenih primjeraka, pod uvjetom da to
dopušta posrednički poslužitelj tvoje organizacije.

## Funkcije

* Podrška za razne vrste posredničkih poslužitelja: http, socks4 i socks5.
* Sposobnost preusmjeravanja cjelokupnog prometa putem posredničkog
  poslužitelja ili samo određenog prometa (http, https, ftp).
* Sposobnost preusmjeravanja cjelokupnog prometa putem posredničkog
  poslužitelja i nakon toga, preusmjeravanje određenog prometa putem drugih
  poslužitelja (ugniježđeni posrednički poslužitelji).
* Prepoznavanje profila i postavki konfiguracija: ako uglavnom radiš s
  prijenosnom kopijom NVDA čitača, možeš stvoriti razne profile za različita
  okruženja (dom, posao, ured1, ured2), te ih ručno aktivirati.

## Upotreba

Ovaj dodatak dodaje novu kategoriju u dijalogu NVDA postavki pod nazivom
„Posrednik”. U ovoj kategoriji pronaći ćeš četiri grupe postavki. Prva
omogućuje konfiguriranje općeg posrednika za sav promet. Ostale grupe
omogućuju konfiguriranje posredničkog poslužitelja za određene
protokole. Sve grupe imaju sljedeća polja:

* Računalo: ime računala ili ip adresa posredničkog poslužitelja. Ostavi
  prazno za deaktiviranje tog posrednika.
* Priključak: priključak poslužitelja.
* Korisničko ime: neobavezno. Korisničko ime za autentifikaciju na
  poslužitelj.
* Lozinka: neobavezno. Lozinka za autentifikaciju na poslužitelj. Lozinka
  nije potrebna za socks4 poslužitelje.

Pored prethodnih polja, u prvoj grupi postavki dostupne su sljedeće
mogućnosti:

* Vrsta SOCKS posrednika: mogu se odabrati socks4, socks5 ili http.
* Ako je moguće, koristi posrednika za dns: kad se ovaj potvrdni okvir
  označi, imena računala ili imena domena izravno će se slati i rješavati na
  posredničkom poslužitelju. Kad se ne označi, imena će se rješavati
  lokalno, a poslužitelj će primiti samo ip adresu odredišta. Ovu opciju ne
  podržavaju svi socks4 posrednički poslužitelji.

Većina korisnika morat će konfigurirati samo prvu grupu postavki. Ako ne
znaš podatke posrednika, zatraži informacije od administratora.

## Ograničenja

* Vrlo ograničena IPV6 podrška.
* UDP promet nije podržan na svim posredničkim poslužiteljima.
* Vanjske DLL biblioteke neće se držati postavaka koje su konfigurirane u
  ovom dodatku.
* Za http posredničke poslužitelje podržana je samo osnovna
  autentifikacija. Sažeta autentifikacija nije podržana.
* Za preusmjeravanje svog prometa (uključujući https veze) putem http
  posrednika, poslužitelj mora podržavati http metodu CONNECT.
* Modus „izravne veze” se ne može konfigurirati. Ako deaktiviraš određenog
  posrednika, umjesto njega će se koristiti standard sustava.

## Zapis promjena

### Verzija 1.2

* Kompatibilno s NVDA 2023.1.
* Iz sigurnosnih razloga, minimalna NVDA verzija postavljena je na 2022.4.
* Aktualizirani prijevodi.

### Verzija 1.1

* Kompatibilno s NVDA čitačem 2022.1.
* Iz sigurnosnih razloga, minimalna NVDA verzija postavljena je na 2021.3.
* Zakrpa funkcije „socket.getaddrinfo” kad je potvrdni okvir „Ako je moguće,
  koristi posrednika za dns” aktiviran i ako je konfiguriran opći posrednik.

### Verzija 1.0

* Prvo izdanje.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=proxy
