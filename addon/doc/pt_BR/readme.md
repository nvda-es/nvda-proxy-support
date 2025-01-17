[[!meta title=“Suporte a proxy para NVDA”]].

* Autor: Jose Manuel Delicado
* Compatibilidade com NVDA: 2023.3.4 e posterior
* Download [versão estável][1]

Esse complemento permite que o leitor de tela NVDA se conecte à Internet por
meio de um ou mais servidores proxy. Para que isso seja possível, ele aplica
vários patches à biblioteca Python padrão ou modifica determinadas variáveis
de ambiente, dependendo da configuração escolhida. Você poderá atualizar o
NVDA e seus complementos automaticamente a partir do seu ambiente
corporativo e até mesmo realizar sessões remotas, desde que o servidor proxy
da sua organização permita isso.

## Recursos

* Suporte a vários tipos de servidores proxy: http, socks4 e socks5.
* Capacidade de redirecionar todo o tráfego por meio do servidor proxy ou
  somente tráfego específico (http, https, ftp).
* Capacidade de redirecionar todo o tráfego por meio de um servidor proxy e,
  depois disso, redirecionar o tráfego específico por meio de outros
  servidores (proxies aninhados).
* Alternância de perfil e redefinição de configuração: se você costuma
  trabalhar com uma cópia portátil do NVDA, pode criar vários perfis para
  diferentes ambientes (casa, trabalho, escritório 1, escritório 2) e
  ativá-los manualmente.

## Uso

Esse complemento adiciona uma nova categoria à caixa de diálogo de
configurações do NVDA chamada “Proxy”. Nessa categoria, você encontrará
quatro grupos de configurações. O primeiro permite que você configure um
proxy geral para todo o tráfego. Os outros grupos permitem que você
configure servidores proxy somente para protocolos específicos. Todos os
grupos têm os seguintes campos:

* Servidor: nome do servidor ou endereço IP do servidor proxy. Deixe em
  branco para desativar esse proxy específico.
* Porta: porta do servidor.
* Nome de usuário: opcional. Nome de usuário para autenticação do servidor.
* Senha: opcional. Senha para autenticação do servidor. Observe que a senha
  não é necessária para servidores socks4.

Além dos campos anteriores, as seguintes opções estão disponíveis no
primeiro grupo de configurações:

* Tipo de proxy SOCKS: socks4, socks5 ou http podem ser selecionados.
* Use proxy para solicitações de DNS, se possível: quando essa caixa de
  seleção estiver marcada, os nomes de servidor ou de domínio serão enviados
  diretamente para o servidor proxy e resolvidos nele. Quando ela estiver
  desmarcada, os nomes serão resolvidos localmente e o servidor receberá
  apenas o endereço IP de destino. Observe que nem todos os servidores proxy
  socks4 suportam essa opção.

De modo geral, a maioria dos usuários só precisará configurar o primeiro
grupo de configurações. Se não souber os detalhes do seu proxy, peça mais
informações ao administrador de rede da sua organização.

## Limitações

* Suporte muito limitado a IPV6.
* O tráfego UDP não é suportado em todos os servidores proxy.
* As bibliotecas DLL externas não respeitarão as configurações definidas
  nesse complemento.
* Somente a autenticação básica é compatível com os servidores proxy http. A
  autenticação Digest não é compatível.
* Para redirecionar todo o tráfego (inclusive conexões https) por meio de um
  proxy http, o servidor deve ser compatível com o método CONNECT http.
* Não é possível configurar um modo de “conexão direta”. Se você desativar
  um proxy específico, o padrão do sistema será usado em seu lugar.

## Registro de alterações

### Versão 1.2

* Compatível com o NVDA 2023.1.
* Por motivos de segurança, a versão mínima do NVDA está definida como
  2022.4.
* Traduções atualizadas.

### Versão 1.1

* Compatível com o NVDA 2022.1.
* Por motivos de segurança, a versão mínima do NVDA está definida como
  2021.3.
* Correção da função socket.getaddrinfo quando a caixa de seleção “Use proxy
  para solicitações de DNS, se possível” estiver marcada e um proxy geral
  tiver sido configurado.

### Versão 1.0

* Lançamento inicial.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=proxy
