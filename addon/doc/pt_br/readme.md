# Suporte de proxy para NVDA

## Introdução

Este extra permite que o leitor de ecrã NVDA se ligue à Internet através de um ou mais servidores proxy. Para fazer isso, aplica vários patches à biblioteca padrão do Python ou modifica certas variáveis de ambiente, dependendo da configuração escolhida. Pode actualizar o NVDA e os seus extras automaticamente a partir do seu local de trabalho e até mesmo realizar sessões remotas, desde que o servidor proxy da sua empresa o permita.

## Características

* Suporte para vários tipos de servidor proxy: http, socks4 e socks5.
* Capacidade de redireccionar todo o tráfego através do servidor proxy ou apenas tráfego específico (http, https, ftp).
* Capacidade de redireccionar todo o tráfego por meio de um servidor proxy e, em seguida, redireccionar o tráfego específico por meio de outros servidores (proxies aninhados).
* Sensível a alterações de perfil e redefinição de configuração: Se normalmente trabalha com uma cópia portátil do NVDA, pode criar perfis diferentes para ambientes diferentes (casa, trabalho, escritório 1, escritório 2) e activá-los manualmente.

## Modo de uso

O extra adiciona uma nova categoria às opções do NVDA, chamada "Proxy". Nesta categoria, encontraremos quatro grupos de opções. O primeiro permite-nos configurar um proxy geral para todo o tráfego. Os outros três permitem que configure servidores proxy apenas para protocolos específicos. Todos os grupos possuem os seguintes campos:

* Servidor: nome do host ou endereço IP do servidor proxy. Deixe em branco para desabilitar esse proxy específico.
* Porta: porta do servidor.
* Utilizador: opcional. Nome de utilizador para autenticação no servidor.
* Senha: opcional. Senha para autenticação no servidor. Observe que a senha não é necessária nos servidores socks4.

Para além dos campos anteriores, no primeiro grupo de opções podemos encontrar o seguinte:

* Tipo de proxy SOCKS: podemos escolher entre socks4, socks5 e http.
* Use proxy para solicitações de DNS se possível - Se esta caixa estiver marcada, os nomes de host ou domínio serão enviados directamente para o servidor proxy e resolvidos lá. Se desmarcado, os nomes serão resolvidos localmente e o servidor receberá apenas o endereço IP de destino. Observe que nem todos os servidores socks4 suportam esta opção.

Normalmente, a maioria dos utulizadores só precisa configurar o primeiro conjunto de opções. Se não souber os detalhes do seu servidor proxy, verifique com o administrador de rede da sua organização.

## Limitações

* Suporte IPV6 muito limitado.
* O tráfego UDP não é compatível com todos os tipos de servidores proxy.
* Bibliotecas DLL externas não respeitarão as opções configuradas neste extra.
* Em servidores proxy http, apenas a autenticação básica é suportada. A autenticação Digest não é compatível.
* Para redireccionar todo o tráfego (incluindo conexões https) por meio de um proxy http, o servidor deve suportar o método http CONNECT.
* Um modo de "conexão directa" não pode ser definido. Se desabilitar um proxy específico, o proxy padrão do sistema será usado.

## Registo de alterações

### Versão 1.0

* Versão inicial.