# PenseNissoApp

  O Pense Nisso é uma aplicação Web desenvolvida pelo grupo de mesmo nome na disciplina de Engenharia de Software (MC426) da Universidade Estadual de Campinas no 2º semestre de 2023. O projeto teve como base uma atividade concebida na disciplina de Construção de Interfaces Humano-Computador (MC750) no 1º semestre do mesmo ano.

  Consiste em uma plataforma de denúncia web de divulgação sobre más práticas trabalhistas e ambientais de empresas, contando com um banco de dados de processos e notícias sobre esses temas.

## Descrição da Arquitetura

![Diagrama de Componentes](https://drive.google.com/uc?id=1BqpTdHJbgLZbrsy34PVkX_XRL9yqZvku)

A figura acima apresenta o diagrama de componentes para a modelagem da arquitetura usada no projeto. Nesse modelo, um usuário interage com a aplicação web e tem sua requisição tratada pela feature específica.  

O estilo arquitetural básico adotado pelo grupo foi o estilo em camadas. Aqui, existem uma série de níveis de funcionalidades e componentes que interagem entre si de forma hierárquica, de modo que uma dada camada apenas interage com camadas diretamente acima e abaixo. Aqui, foram estabelecidas uma camada do frontend, com a qual o usuário interage diretamente, e três camadas do backend, responsáveis por realizar o processamento e tratamento dos pedidos do usuário.

Outro aspecto importante da organização do código é o estilo definido pelo framework Django usado no desenvolvimento. Esse framework define diretórios especializados, chamados apps, para dividir funcionalidades gerais da aplicação. No caso, cada app apresenta vários arquivos e responsabilidades, configurando, muitas vezes, mais de um componente, conforme mostra a figura. Ademais, o framework define um app especial central, o qual recebe os pedidos do usuário e transfere a responsabilidade para o app especializado adequado, além de ser responsável por uma série de outras configurações gerais da aplicação. Por ser parte mais do framework do que da aplicação em si, ele foi considerado como sendo um único componente dedicado.

Com isso, o grupo definiu quatro camadas principais: a camada do frontend, a camada de redirecionamento, a camada de Views e a camada de Models. Abaixo, segue uma breve descrição da funcionalidade de cada camada.

- **Frontend:** parte visual acessada diretamente pelo usuário através de templates HTML e CSS.
- **Redirecionamento:** administrada principalmente pelo framework, recebe os pedidos vindos do frontend e redireciona-os para os apps apropriados por meio da camada de Views.
- **Views:** camada de entrada dos vários apps desenvolvidos, por onde o pedido do usuário é processado propriamente. Estabelece tratamento de diferentes métodos HTTPS para cada página, e possui protocolos internos para garantir comunicação entre vários apps.
- **Models:** camada de definição e integração de tabelas do banco de dados, com quem interage diretamente. Comunica-se com Views na hora de realizar consultas e adições ao banco de dados.

Abaixo, segue uma lista dos principais componentes da arquitetura, bem como suas responsabilidades e seus respectivos apps.

- **User App:** permite que usuários tenham acesso às funcionalidades relacionadas ao cadastro.
    - **Views (User):** trata a requisição do cliente e o redireciona ao formulário de cadastro ou à página do usuário. Interage com Form (User) e Model (User).
    - **Form (User):** permite que um novo usuário seja criado por meio do fornecimento de dados cadastrais. Interage com Model (User).
    - **Models (User):** administra os modelos de páginas de usuário contidas no banco de dados e as informações nela contidas. Interage diretamente com o banco de dados.
- **Comparator App:** permite que o cliente solicite visualização simultânea de determinadas informações sobre diversas empresas cadastradas na aplicação, permitindo a comparação dos dados apresentados de diversas empresas.
    - **Views (Comparator):** recebe diversos pedidos do cliente para a adição de uma empresa na tela de visualização. Possui integração direta com a busca, permitindo que o usuário pesquise por um nome. Interage com Models (Company) para a coleta dos dados das empresas adicionadas.
- **Search App:** permite que o cliente busque pelo nome de alguma empresa.
    - **Views (Search):** trata a requisição feita pelo usuário e o direciona a uma página com resultados diretamente correspondentes ou semelhantes à busca. Comunica com a Company para definir resultados possíveis e redirecionar o usuário para a empresa correspondente.
- **Company App:** permite ao cliente visualizar a página das empresas cadastradas na aplicação.
    - **Views (Company):** trata a requisição vinda do sistema de buscas (diretamente da barra de pesquisa ou integrada em alguma outra feature da aplicação) ou diretamente do explorador de empresas, e redireciona o cliente à respectiva página. Interage com Models (Company) para exibir e tratar apenas de empresas cadastradas no banco de dados.
    - **Forms (Company):** permite que um usuário preencha um formulário de submissão de sugestão para a adição de uma nova empresa no banco de dados. Interage com Models (Company) para a adição no banco de dados após a aprovação da sugestão.
    - **Models (Company):** administra os modelos de páginas de empresa contidas no banco de dados e as informações nela contidas. Interage diretamente com o banco de dados.
- **Infos App:** administra informações gerais de empresas, como notícias, denúncias e processos. Permite cadastro de novas informações e acesso de informações existentes.
    - **Views (Infos):** recebe o pedido do usuário ou de outro componente e faz o tratamento o direcionando para o formulário de denúncia ou para alguma das páginas contendo notícias, processos e denúncias referentes à empresa. Interage com Forms (Infos) e com os Models de cada tipo de informação presente.
    - **Form (Report):** permite que o cliente submeta uma denúncia sobre a empresa em questão, inserindo a categoria (ambiental ou trabalhista), descrição da reclamação e permissão para contato por parte da moderação.
    - **Models (News):** administra o modelo do banco de dados das notícias sobre a empresa, contendo título, autor e data de publicação.
    - **Models (Lawsuit):** administra o modelo do banco de dados dos processos contra a empresa, incluindo o link com a fonte da informação, ano de abertura e ano de encerramento.
    - **Models (Reports):** administra o modelo do banco de dados das denúncias relativas à empresa em questão, apresentando título, categoria, conteúdo da denúncia, autor, data de criação e de edição.
- **PenseNissoApp:** administrado principalmente pelo framework para o tratamento geral de pedidos do usuário. Interage com todos os componentes do tipo Views.

Para o projeto do componente Views (Infos), o grupo percebeu que haveria repetição de código se para cada tipo de informação fossem criados arquivos separados e independentes. Assim, foi decidido que o padrão de projeto Strategy fosse implementado. Esse padrão de projeto permite reutilizar a base das classes que seria repetida e apenas mudar os detalhes de implementação específicos, facilitando a adição estruturada de novas classes de informações.
