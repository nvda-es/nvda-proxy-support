# Proxy support for NVDA #

* Autor: José Manuel Delicado
* NVDA compatibility: 2021.3 and beyond
* Baixar [versão estável] [1]

Este extra permite ao leitor de ecrã NVDA ligar-se à Internet através de um
ou mais servidores proxy. Para o tornar possível, aplica vários patches à
biblioteca Python padrão ou modifica certas variáveis de ambiente,
dependendo da configuração escolhida. Poderá actualizar o NVDA e os seus
extras automaticamente a partir do seu ambiente corporativo e até realizar
sessões remotas, desde que o servidor proxy da sua organização o permita.

## Funcionalidades

* Suporte para vários tipos de servidores proxy: http, socks4 e socks5.
* Capacidade de redireccionar todo o tráfego através do servidor proxy ou
  apenas tráfego específico (http, https, ftp).
* Capacidade de redireccionar todo o tráfego através de um servidor proxy e,
  depois disso, redireccionar tráfego específico através de outros
  servidores (proxies aninhados).
* Mudança de perfil e reset de configuração personalizados: se trabalha
  habitualmente com uma cópia portátil do NVDA, pode criar vários perfis
  para diferentes ambientes (casa, trabalho, escritório1, escritório2) e
  activá-los manualmente.

## Modo de uso

Este extra adiciona uma nova categoria ao diálogo de configurações do NVDA
chamado "Proxy". Nesta categoria, encontrará quatro grupos de
configurações. O primeiro permite configurar um proxy geral para todo o
tráfego. Os outros grupos permitem-lhe configurar servidores proxy apenas
para protocolos específicos. Todos os grupos têm os seguintes campos:

* Host: hostname ou endereço ip do servidor proxy. Deixar vazio para
  desactivar esse proxy em particular.
* Porta: porta do servidor.
* Nome de utilizador: opcional. Nome de utilizador para autenticação do
  servidor.
* Senha: opcional. Palavra-passe para autenticação do servidor. Note que a
  palavra-passe não é necessária para os servidores Socks4.

Para além dos campos anteriores, estão disponíveis as seguintes opções no
primeiro grupo de configurações:

* SOCKS tipo proxy: socks4, socks5 ou http podem ser seleccionados.
* Utilizar proxy para solicitações dns se possível: quando esta caixa de
  verificação for marcada, os nomes de hosts ou nomes de domínio serão
  enviados directamente para o servidor proxy e resolvidos no servidor
  proxy. Quando não estiver marcada, os nomes serão resolvidos localmente e
  o servidor receberá apenas o endereço ip de destino. Note-se que nem todos
  os servidores proxy Socks4 suportam esta opção.

fundamentalmente, a maioria dos utilizadores apenas terá de configurar o
primeiro grupo de configurações. Se não conhece os seus dados de proxy, peça
mais informações ao administrador da rede da sua organização.

## Limitações

* Suporte IPV6 muito limitado.
* O tráfego UDP não é suportado em todos os servidores proxy.
* As bibliotecas DLL externas não respeitarão as definições configuradas
  neste add-on.
* Apenas a autenticação básica é suportada para servidores proxy http. A
  autenticação digest não é suportada.
* A fim de redireccionar todo o tráfego (incluindo ligações https) através
  de um proxy http, o servidor deve suportar o método CONNECT http.
* Um modo de "ligação directa" não pode ser configurado. Se desactivar um
  proxy específico, será utilizado em vez disso o padrão do sistema.

## Alterações

### Version 1.1

* Compatible with NVDA 2022.1.
* For security reasons, minimum NVDA version is set to 2021.3.
* Patch socket.getaddrinfo function when "Use proxy for dns requests if
  possible" checkbox is checked and a general proxy has been configured.

### Versão 1.0

* Lançamento inicial.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=nvdaproxy
