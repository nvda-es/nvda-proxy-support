# Proxy support for NVDA

* Author: José Manuel Delicado
* NVDA compatibility: 2021.3 and beyond
* Download [stable version][1]

This add-on allows the NVDA screen reader to connect to the Internet through one or more proxy servers. To make it possible, it applies various patches to the standard Python library or modifies certain environment variables, depending on the chosen configuration. You will be able to update NVDA and their add-ons automatically from your corporate environment and even perform remote sessions, provided that your organization proxy server allows it.

## Features

* Support for various proxy server types: http, socks4 and socks5.
* Ability to redirect all traffic through the proxy server or only specific traffic (http, https, ftp).
* Ability to redirect all traffic through a proxy server and, after that, redirect specific traffic through other servers (nested proxies).
* Profile switch and config reset aware: if you usually work with a portable copy of NVDA, you can create various profiles for different environments (home, work, office1, office2) and manually activate them.

## Usage

This add-on adds a new category to the NVDA settings dialog called "Proxy". In this category, you will find four settings groups. The first one allows you to configure a general proxy for all traffic. The other groups allow you to configure proxy servers only for specific protocols. All groups have the following fields:

* Host: hostname or ip address of the proxy server. Leave empty to disable that particular proxy.
* Port: server port.
* Username: optional. User name for server autentication.
* Password: optional. Password for server autentication. Note that password is not required for socks4 servers.

In addition to the previous fields, the following options are available in the first settings group:

* SOCKS proxy type: socks4, socks5 or http can be selected.
* Use proxy for dns requests if possible: when this checkbox is checked, hostnames or domain names will be directly sent to and resolved on the proxy server. When it is unchecked, names will be resolved locally and the server will receive only the destination ip address. Note that not all socks4 proxy servers support this option.

Tipically, most users will only have to configure the first settings group. If you don't know your proxy details, ask your organization network administrator for more information.

## Limitations

* Very limited IPV6 support.
* UDP traffic is not supported on all proxy servers.
* External DLL libraries won't respect the settings configured in this add-on.
* Only basic autentication is supported for http proxy servers. Digest autentication is not supported.
* In order to redirect all traffic (including https connections) through an http proxy, the server must support the CONNECT http method.
* A "direct connection" mode can't be configured. If you disable a specific proxy, the system default will be used instead.

## Changelog

### Version 1.1

* Compatible with NVDA 2022.1.
* For security reasons, minimum NVDA version is set to 2021.3.
* Patch socket.getaddrinfo function when "Use proxy for dns requests if possible" checkbox is checked and a general proxy has been configured.
* Updated translations.

### Version 1.0

* Initial release.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=nvdaproxy
