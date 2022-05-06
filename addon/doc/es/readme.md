# Soporte proxy para NVDA #

* Autor: José Manuel Delicado
* Compatibilidad con NVDA: de 2021.3 en adelante
* Descargar [versión estable][1]

Este complemento permite que el lector de pantalla NVDA pueda conectarse a
Internet a través de uno o varios servidores proxy. Para ello, aplica
diversos parches a la biblioteca estándar de Python o modifica ciertas
variables de entorno, dependiendo de la configuración elegida. Podrás
actualizar NVDA y sus complementos automáticamente desde tu entorno
corporativo, e incluso realizar sesiones remotas, siempre que el servidor
proxy de tu organización lo permita.

## Características

* Soporte para diversos tipos de servidor proxy: http, socks4 y socks5.
* Capacidad de redirigir todo el tráfico a través del servidor proxy o sólo
  tráfico específico (http, https, ftp).
* Capacidad de redirigir todo el tráfico a través de un servidor proxy, y
  después redirigir tráfico específico a través de otros servidores (proxies
  anidados).
* Sensible a cambios de perfil y restablecimiento de configuración: si
  normalmente trabajas con una copia portátil de NVDA, puedes crear diversos
  perfiles para distintos entornos (casa, trabajo, oficina 1, oficina 2) y
  activarlos manualmente.

## Modo de uso

El complemento añade una nueva categoría a las opciones de NVDA, llamada
"Proxy". En esta categoría encontraremos cuatro grupos de opciones. El
primero nos permite configurar un proxy general para todo el tráfico. Los
otros tres permiten configurar servidores proxy sólo para protocolos
específicos. Todos los grupos tienen los siguientes campos:

* Servidor: nombre de host o dirección ip del servidor proxy. Déjalo vacío
  para deshabilitar ese proxy en particular.
* Puerto: puerto del servidor.
* Usuario: opcional. Nombre de usuario para autenticarse en el servidor.
* Contraseña: opcional. Contraseña para autenticarse en el servidor. Ten en
  cuenta que la contraseña no es necesaria en servidores socks4.

Además de los campos anteriores, en el primer grupo de opciones podemos
encontrar los siguientes:

* Tipo de proxy SOCKS: podemos elegir entre socks4, socks5 y http.
* Usar proxy para solicitudes DNS si es posible: si esta casilla está
  marcada, los nombres de host o dominio se enviarán directamente al
  servidor proxy y se resolverán allí. Si está desmarcada, los nombres se
  resolverán localmente y el servidor sólo recibirá la dirección ip de
  destino. Ten en cuenta que no todos los servidores socks4 soportan esta
  opción.

Normalmente, la mayoría de usuarios sólo tendrán que configurar el primer
grupo de opciones. Si no conoces los detalles de tu servidor proxy, consulta
con el administrador de red de tu organización.

## Limitaciones

* Soporte IPV6 muy limitado.
* El tráfico UDP no se soporta en todos los tipos de servidores proxy.
* Las bibliotecas DLL externas no respetarán las opciones configuradas en
  este complemento.
* En servidores proxy http, sólo se soporta autenticación básica. La
  autenticación digest no está soportada.
* Para poder redirigir todo el tráfico (incluyendo conexiones https) a
  través de un proxy http, el servidor debe soportar el método http CONNECT.
* No se puede configurar un modo de "conexión directa". Si deshabilitas un
  proxy específico, se usará en su lugar el proxy por defecto del sistema.

## Registro de cambios

### Versión 1.1

* Compatible con NVDA 2022.1.
* Por motivos de seguridad, se ha establecido la versión mínima de NVDA a
  2021.3.
* Se parchea la función socket.getaddrinfo cuando se marca la casilla "Usar
  proxy para solicitudes DNS si es posible" y se configura un proxy general.

### Versión 1.0

* Versión inicial.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=nvdaproxy
