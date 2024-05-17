# Proxy-Unterstützung für NVDA #

* Autor: José Manuel Delicado
* NVDA compatibility: 2023.3.4 and beyond
* [Stabile Version] herunterladen[1]

Mit dieser NVDA-Erweiterung können Sie Verbindungen über eine oder mehrere
Proxy-Server mit dem Internet herstellen. Um dies zu ermöglichen, wendet es
je nach gewählter Konfiguration verschiedene Patches auf die
Standard-Python-Bibliothek an oder modifiziert bestimmte
Umgebungsvariablen. Sie können NVDA und deren Erweiterungen automatisch aus
Ihrer Unternehmensumgebung aktualisieren und sogar Remote-Sitzungen
durchführen, sofern der Proxy-Server Ihres Unternehmens dies zulässt.

## Features

* Unterstützung für verschiedene Proxy-Server-Typen: HTTP, Socks4/5.
* Möglichkeit, den gesamten Datenverkehr über den Proxy-Server oder nur
  bestimmten Datenverkehr (HTTP, HTTPS, FTP) umzuleiten.
* Möglichkeit, den gesamten Datenverkehr über einen Proxy-Server umzuleiten
  und danach bestimmten Datenverkehr über andere Server (verschachtelte
  Proxys) umzuleiten.
* Profilwechsel und Möglichkeit die Konfiguration zurückzusetzen: Wenn Sie
  normalerweise mit einer portablen NVDA-Version arbeiten, können Sie
  verschiedene Profile für verschiedene Umgebungen (Heim, Arbeit, Büro1,
  Büro2) erstellen und manuell aktivieren.

## Anwendung

Diese Erweiterung fügt dem NVDA-Einstellungsdialog eine neue Kategorie mit
dem Namen "Proxy" hinzu. In dieser Kategorie finden Sie vier
Einstellungsgruppen. Mit dem ersten können Sie einen allgemeinen Proxy für
den gesamten Datenverkehr konfigurieren. Mit den anderen Gruppen können Sie
Proxyserver nur für bestimmte Protokolle konfigurieren. Alle Gruppen haben
die folgenden Felder:

* Host: Hostname oder IP-Adresse des Proxyservers. Lassen Sie das Feld leer,
  um diesen bestimmten Proxy zu deaktivieren.
* Port: Server-Port.
* Benutzername: Optional. Benutzername für die Server-Authentifizierung.
* Passwort: Optional. Passwort für die Server-Authentifizierung. Beachten
  Sie, dass für Socks4-Server kein Kennwort erforderlich ist.

Zusätzlich zu den vorherigen Feldern stehen in der ersten Einstellungsgruppe
folgende Optionen zur Verfügung:

* SOCKS-Proxy-Typ: Socks4/5 oder HTTP können ausgewählt werden.
* Nach Möglichkeit einen Proxy für DNS-Anfragen verwenden: Wenn dieses
  Kontrollkästchen aktiviert ist, werden Hostnamen oder Domänennamen direkt
  an den Proxy-Server gesendet und dort aufgelöst. Wenn es deaktiviert ist,
  werden Namen lokal aufgelöst und der Server erhält nur die
  Ziel-IP-Adresse. Beachten Sie, dass nicht alle socks4-Proxyserver diese
  Option unterstützen.

Normalerweise müssen die meisten Benutzer nur die erste Einstellungsgruppe
konfigurieren. Wenn Sie Ihre Proxy-Details nicht kennen, fragen Sie den
Netzwerkadministrator Ihres Unternehmens nach weiteren Informationen.

## Einschränkungen

* Sehr eingeschränkte IPv6-Unterstützung.
* UDP-Datenverkehr wird nicht auf allen Proxyservern unterstützt.
* Externe Programm-Bibliotheken berücksichtigen die in dieser Erweiterung
  konfigurierten Einstellungen nicht.
* Für HTTP-Proxyserver wird nur die grundlegende Authentifizierung
  unterstützt. Die Digest-Authentifizierung wird nicht unterstützt.
* Um den gesamten Datenverkehr (einschließlich HTTPS-Verbindungen) über
  einen http-Proxy umzuleiten, muss der Server die HTTP-Methode CONNECT
  unterstützen.
* Ein Modus "Direktverbindung" kann nicht konfiguriert werden. Wenn Sie
  einen bestimmten Proxy deaktivieren, wird stattdessen der Systemstandard
  verwendet.

## Änderungsprotokoll

### Version 1.2

* Kompatibel mit NVDA 2023.1.
* Aus Sicherheitsgründen ist die Mindestversion von NVDA auf 2022.4
  festgelegt.
* Aktualisierte Übersetzungen.

### Version 1.1

* Kompatibel mit NVDA 2022.1.
* Aus Sicherheitsgründen wurde die Minimum-Version von NVDA auf 2021.3
  festgelegt.
* Patch der Funktion "socket.getaddrinfo", wenn das Kontrollkästchen "Nach
  Möglichkeit einen Proxy für DNS-Anfragen verwenden" aktiviert ist und ein
  allgemeiner Proxy konfiguriert ist.

### Version 1.0

* Erstveröffentlichung.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=proxy
