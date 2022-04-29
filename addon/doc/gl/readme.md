# Soporte proxy para NVDA #

* Autor: Jose Manuel Delicado
* Compatibilidade co NVDA: da 2019.3 á 2021.1
* Descargar [versión estable][1]

Este complemento permite ó lector de pantallas NVDA conectarse á Internet a
través dun ou máis servidores proxy. Para que isto sexa posible, aplica
varios parches á librería estándar de Python ou modifica certas variables de
entorno, dependendo da configuración escollida. Poderás actualizar NVDA e os
seus automaticamente dende o teu entorno corporativo e mesmo realizar
sesions remotas, sempre que o servidor proxy da túa organización as permita.

## Características

* Soporte para varios tipos de servidor proxy: http, socks4 e socks5.
* Capacidade de redirixir todo o tráfico a través do servidor proxy ou só
  tráfico específico (http, https, ftp).
* Capacidade para redirixir todo o tráfico a través dun servidor proxy e,
  despois, redirixir tráfico específico a través doutros servidores (proxys
  anidados).
* Sensible a trocos de perfil e restablecementos de configuración: se
  normalmente traballas cunha copia portable de NVDA, podes crear varios
  perfís para diferentes entornos (casa, traballo, oficina1, oficina2) e
  activalos manualmente.

## Uso

Este complemento engade unha nova categoría ó diálogo de opcións de NVDA
chamada "Proxy". Nesta categoría, atoparás catro grupos de axustes. O
primeiro permíteche configurar un proxy xeral para todo o tráfico. Os outros
grupos permítenche configurar só para protocolos específicos. todos os
grupos teñen os seguintes campos:

* Host (servidor): nome de servidor ou enderezo IP do servidor proxy. déixao
  en blanco para deshabilitar ese proxy en concreto.
* Port (porto): porto do servidor.
* Username (nome de usuario): opcional. Nome de usuario para autenticación
  no servidor.
* Password (contrasinal): opcional. contrasinal para a autenticación no
  servidor. Ten en conta que o contrasinal non se require en servidores
  socks4.

Ademais dos anteriores campos, están dispoñibles as seguintes opcións no
primeiro grupo de axustes:

* SOCKS proxy type (tipo de servidor SOCKS): pódese seleccionar socks4,
  socks5 ou http.
* Use proxy for dns requests if possible (utilizar proxy para solicitudes
  DNS cando sexa posible): cando esta caixa estea marcada, os nomes de
  servidor ou de dominio enviaranse a e resolveranse directamente no
  servidor proxy. Cando estea desmarcada, os nomes resolveranse localmente e
  o servidor recibirá só o enderezo IP de destino. Ten en conta que non
  todos os servidores socks4 soportan esta opción.

Normalmente, a maioría de usuarios só terán que configurar o primeiro grupo
de axustes. Se non coñeces os detalles do teu proxy, consulta ó
administrador da rede da organización para máis información.

## Limitacións

* Soporte IPV6 moi limitado.
* O tráfico UDP non está soportado en ningún dos servidores proxy.
* Bibliotecas DLL externas non respectarán os axustes configurados neste
  complemento.
* Só se soporta autenticación básica en servidores proxy http. Non se
  soporta autenticación digest.
* Para redirixir todo o tráfico (incluíndo conexións https) a través dun
  proxy http, o servidor debe soportar o método http CONNECT.
* Non se pode configurar un modo de "conexión directa". Se deshabilitas un
  proxy en específico, utilizarase o predeterminado do sistema.

## Rexistro de trocos

### Versión 1.0

* Publicación inicial.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=nvdaproxy
