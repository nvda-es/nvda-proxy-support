# Proxy support for NVDA #

* Autor: Jose Manuel Delicado
* Zgodność z NVDA: 2021.3 i później
* Pobierz [Wersja stabilna][1]

Ten dodatek umożliwia czytnikowi ekranu NVDA łączenie się z Internetem za
pośrednictwem jednego lub więcej serwerów proxy. Aby było to możliwe,
stosuje różne poprawki do standardowej biblioteki Pythona lub modyfikuje
pewne zmienne środowiskowe, w zależności od wybranej konfiguracji. Będziesz
mógł automatycznie aktualizować NVDA i ich dodatki ze środowiska
korporacyjnego, a nawet wykonywać zdalne sesje, pod warunkiem, że zezwala na
to serwer proxy Twojej organizacji.

## Funkcje

* Obsługa różnych typów serwerów proxy: http, socks4 i socks5.
* Możliwość przekierowania całego ruchu przez serwer proxy lub tylko
  określony ruch (http, https, ftp).
* Możliwość przekierowywania całego ruchu przez serwer proxy, a następnie
  przekierowywania określonego ruchu przez inne serwery (zagnieżdżone
  serwery proxy).
* Przełączanie profili i resetowanie konfiguracji: jeśli zwykle pracujesz z
  przenośną kopią NVDA, możesz utworzyć różne profile dla różnych środowisk
  (dom, praca, biuro1, biuro2) i ręcznie je aktywować.

## Użycie

Ten dodatek dodaje nową kategorię do okna dialogowego ustawień NVDA o nazwie
"Proxy". W tej kategorii znajdziesz cztery grupy ustawień. Pierwszy z nich
pozwala skonfigurować ogólny serwer proxy dla całego ruchu. Pozostałe grupy
umożliwiają konfigurowanie serwerów proxy tylko dla określonych
protokołów. Wszystkie grupy mają następujące pola:

* Host: nazwa hosta lub adres IP serwera proxy. Pozostaw puste, aby wyłączyć
  ten konkretny serwer proxy.
* Port: port serwera.
* Nazwa użytkownika: opcjonalnie. Nazwa użytkownika do uwierzytelniania
  serwera.
* Hasło: opcjonalnie. Hasło do uwierzytelniania serwera. Pamiętaj, że hasło
  nie jest wymagane dla serwerów socks4.

Oprócz poprzednich pól w pierwszej grupie ustawień dostępne są następujące
opcje:

* Można wybrać typ proxy SOCKS: socks4, socks5 lub http.
* Jeśli to możliwe, użyj proxy dla żądań dns: gdy to pole wyboru jest
  zaznaczone, nazwy hostów lub nazwy domen będą bezpośrednio wysyłane i
  rozpoznawane na serwerze proxy. Gdy nie jest zaznaczona, nazwy będą
  rozpoznawane lokalnie, a serwer otrzyma tylko docelowy adres IP. Należy
  pamiętać, że nie wszystkie serwery proxy socks4 obsługują tę opcję.

Co ciekawe, większość użytkowników będzie musiała skonfigurować tylko
pierwszą grupę ustawień. Jeśli nie znasz szczegółów serwera proxy, poproś
administratora sieci organizacji o więcej informacji.

## Ograniczenia

* Bardzo ograniczona obsługa IPV6.
* Ruch UDP nie jest obsługiwany na wszystkich serwerach proxy.
* Zewnętrzne biblioteki DLL nie będą respektować ustawień skonfigurowanych w
  tym dodatku.
* Tylko uwierzytelnianie podstawowe jest obsługiwane dla serwerów proxy
  http. Uwierzytelnianie szyfrowane nie jest obsługiwane.
* Aby przekierować cały ruch (w tym połączenia https) przez serwer proxy
  http, serwer musi obsługiwać metodę CONNECT http.
* Nie można skonfigurować trybu "bezpośredniego połączenia". Jeśli wyłączysz
  określony serwer proxy, zamiast niego zostanie użyty system domyślny.

## Lista zmian

### Wersja 1.1

* Kompatybilny z NVDA 2022.1.
* Ze względów bezpieczeństwa minimalna wersja NVDA jest ustawiona na 2021.3.
* Funkcja Patch socket.getaddrinfo, gdy zaznaczone jest pole wyboru "Użyj
  serwera proxy dla żądań dns, jeśli to możliwe" i skonfigurowano ogólny
  serwer proxy.

### Wersja 1.0

* Wersja pierwotna.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=nvdaproxy
