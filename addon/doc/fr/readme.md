# Support Proxy pour NVDA #

* Auteur : Jose Manuel Delicado
* NVDA compatibility: 2021.3 and beyond
* Télécharger [version stable][1]

Cette extension permet au lecteur d'écran NVDA de se connecter à Internet
via un ou plusieurs serveurs proxy. Pour ce faire, appliquez divers
correctifs dans la bibliothèque standard Python ou modifiez certaines
variables d'environnement, en fonction de la configuration choisie. Vous
pouvez mettre à jour NVDA et ses extensions automatiquement à partir de
votre environnement d'entreprise et même effectuer des sessions distantes,
tant que le serveur proxy de votre organisation le permet.

## Fonctionnalités

* Support de différents types de serveur proxy : http, socks4 et socks5.
* Possibilité de rediriger tout le trafic via le serveur proxy ou uniquement
  du trafic spécifique (http, https, ftp).
* Possibilité de rediriger tout le trafic via un serveur proxy, puis
  rediriger un trafic spécifique à travers d'autres serveurs (proxy
  imbriqués).
* Sensible aux modifications de profil et à la réinitialisation de la
  configuration : Si vous travaillez normalement avec une copie portable de
  NVDA, vous pouvez créer divers profils pour différents environnements
  (maison, travail, bureau 1, bureau 2) et les activer manuellement.

## Utilisation

Cette extension ajoute une nouvelle catégorie aux paramètres de NVDA,
appelée "Proxy". Dans cette catégorie, nous trouverons quatre groupes
d'options. Le premier nous permet de configurer un proxy général  pour tout
le trafic. Les trois autres permettent de configurer des serveurs proxy
uniquement pour des protocoles spécifiques. Tous les groupes ont les champs
suivants :

* Serveur : Nom d'hôte ou adresse IP du serveur proxy. Laissez-le vide pour
  désactiver ce proxy en particulier.
* Port : Port du serveur.
* Username: optional. User name for server authentication.
* Password: optional. Password for server authentication. Note that password
  is not required for socks4 servers.

Outre les champs précédents, dans le premier groupe d'options, on trouve les
options suivantes :

* Type de proxy SOCKS : Nous pouvons choisir entre socks4, socks5 et http.
* Utiliser le proxy pour les requêtes DNS si cela est possible : Si cette
  case est cochée, les noms d'hôte ou de domaine seront envoyés directement
  sur le serveur proxy et seront résolus là-bas. Si cette case est décochée,
  les noms seront résolus localement et le serveur ne recevra que l'adresse
  IP de destination. Notez que tous les serveurs socks4 ne supportent pas
  cette option.

Normalement, la plupart des utilisateurs devront seulement configurer le
premier groupe d'options. Si vous ne connaissez pas les détails de votre
serveur proxy, voir avec l'administrateur réseau de votre organisation.

## Limitations

* Support IPV6 très limité.
* Le trafic UDP n'est pas supporté sur tous les types de serveurs proxy.
* Les bibliothèques DLL externes ne respecteront pas les options configurées
  dans cette extension.
* Only basic authentication is supported for http proxy servers. Digest
  authentication is not supported.
* Afin de rediriger tout le trafic (y compris les connexions https) via un
  proxy http, le serveur doit supporter la méthode http CONNECT.
* Vous ne pouvez pas configurer de mode "connexion directe". Si vous
  désactivez un proxy spécifique, le proxy par défaut du système sera
  utilisé à la place.

## Journal des changements

### Version 1.1

* Compatible with NVDA 2022.1.
* For security reasons, minimum NVDA version is set to 2021.3.
* Patch socket.getaddrinfo function when "Use proxy for dns requests if
  possible" checkbox is checked and a general proxy has been configured.

### Version 1.0

* Version initiale.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=nvdaproxy
