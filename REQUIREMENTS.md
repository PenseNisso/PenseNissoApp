# Atividade 3: Elicitação de Requisitos

O presente documento tem como objetivo a especificação de requisitos gerais obtidos por uma série de processos de elicitação de requisitos com base na temática geral da aplicação desenvolvida pelo grupo.

Nesse contexto, deve-se lembrar da ideia geral da aplicação, cujo desenvolvimento, em princípio, já foi iniciado: uma plataforma *online* que permite o acesso a denúncias, processos e notícias relacionados a questões trabalhistas e ambientais de empresas. O *site* permite que usuários acessem conteúdo existente e também realizem novas denúncias, fornecendo informações importantes para o combate às más práticas e em prol do consumo consciente.

Para obtermos os requisitos, foram realizadas duas atividades separadas, uma de *brainstorming* e outra de *benchmarking*.

## Primeira Atividade de Elicitação de Requisitos: Brainstorm / Brainwrite

A primeira atividade realizada para levantar os principais requisitos da aplicação foi a de *brainstorm*. Ao invés do *brainstorming* comum, foi realizada uma variação chamada *brainwrite*, a qual permite que cada participante escreva ideias para uma discussão geral depois. Essa atividade foi realizada por meio da ferramenta do *Jamboard*, permitindo interação e edição em tempo real de cartões virtuais, simulando um ambiente presencial em que cada participante teria uma folha de papel.

Para garantir que os objetivos da atividade fossem alcançados, como a obtenção de requisitos pertinentes, o primeiro passo foi definir uma série de regras a serem seguidas. Para tanto, foi criado um cartão inicial com as regras definidas. Até que todas as dúvidas relacionadas ao procedimento fossem sanadas, a atividade não foi iniciada.

![Cartão com as regras do *brainwrite*](https://drive.google.com/uc?id=1BVAY_CDRaN4_RR4-h-HQ_B77ZHBYiuOQ)

*Cartão com as regras.*

A atividade consiste em uma série de rodadas cronometradas. Em cada rodada, cada participante possui em mãos um cartão. Nele, ele coloca as ideias de funcionalidades que tem. Ao final do tempo, o cartão é passado para um outro integrante. Com o novo cartão, cada um coloca mais ideias, ou expande as ideias presentes. Quando todos receberam e interagiram com todos os cartões, a atividade acaba, e há um debate geral sobre as ideias, em que cada membro expõe o que pensou e novas ideias são geradas.

Para a geração de ideias inicial, foi realizada uma rodada de 5 minutos, e as rodadas subsequentes foram de dois minutos. Com o intuito de facilitar a identificação da ideia de cada membro, cada um usou uma cor diferente para escrever. Ao final do processo, cada cartão continha uma multitude de ideias e sugestões. O resultado pode ser visto [aqui](https://jamboard.google.com/d/1HvP0yF-uIssg4kVc8eSH1QR_mANP1fLaWC37UD3l8QY/edit?usp=sharing).

Com base nas ideias obtidas, o grupo realizou uma discussão em cima de cada cartão, verificando ideias que eram mais pertinentes e adicionando outras contribuições. Com isso, foi possível extrair uma série de requisitos básicos, os quais poderiam depois ser formalizados e convertidos em histórias dos usuários.

### Requisitos

- O sistema deve ter a opção de pesquisa de empresas;
- O usuário deve ser capaz de explorar todas as empresas cadastradas;
- O sistema deve oferecer a opção de filtragem para pesquisas;
- O sistema deve oferecer diversas opções de filtros de pesquisa;
- O usuário deve poder adicionar uma empresa à sua lista de empresas favoritas;
- O sistema deve oferecer um sistema de comparação de empresas;
- O sistema de comparação deve poder comparar um número arbitrário de empresas;
- O sistema deve permitir que um usuário encontre empresas de um dado setor a partir da página da empresa;
- A página principal da aplicação deve fornecer a opção de denúncia diretamente;
- O usuário deve poder optar por receber notificações sobre notícias gerais da aplicação e notícias de empresas seguidas;
- O sistema de busca deve ser capaz de detectar erros de grafia;
- A página inicial da aplicação deve ter uma navegação intuitiva e simples;
- Os moderadores devem ser capazes de cadastrar novas empresas no sistema;
- O comparador deve possuir um sistema de filtragem de empresas;
- O explorador deve possuir um sistema de filtragem de empresas;
- O filtro do explorador também deve permitir ordenação de empresas como desejado pelo usuário;
- O comparador de empresas deve fornecer informações sobre as principais denúncias e a nota de cada empresa;
- O usuário deve ser capaz de ver notícias, processos e denúncias de uma dada empresa;
- Um moderador deve ser capaz de validar denúncias enviadas por usuários;
- A tela de busca deve ter uma opção para levar o usuário ao formulário de inclusão de empresa caso uma empresa cadastrada não seja encontrada;
- O usuário deve ser capaz de ver as denúncias feitas por ele, caso tenha escolhido fazer essas denúncias enquanto logado;
- O usuário deve ser capaz de enviar uma denúncia anonimamente caso ele não esteja logado;
- O usuário deve ser capaz de ver se as denúncias que ele enviou foram aprovadas ou rejeitadas pelos moderadores, ou se ainda estão sob análise.
- A página inicial da aplicação deve possuir um campo de apresentação de notícias gerais no contexto de boas e más práticas empresariais;
- O usuário que não estiver logado deve ser notificado da opção de fazer o cadastro no momento da denúncia;
- A página inicial deve permitir a navegação direta para todas as principais funcionalidades do sistema;
- O sistema deve oferecer duas avaliações para o usuário, uma gerada pelo sistema e outra composta por envios de usuários;
- O usuário pode atribuir uma nota para uma empresa caso esteja logado no sistema;
- O usuário deve ser capaz de criar uma conta no sistema;
- O sistema deve deixar claro quais os critérios de avaliação usados;
- O usuário deve ser capaz de favoritar uma ou mais notícias;
- O usuário poder salvar configurações de empresas no comparador para acesso posterior;
- O usuário pode acessar as notícias e processos de maior notoriedade de uma empresa a partir da ferramenta de comparação.

## Segunda Atividade de Elicitação de Requisitos: Benchmark

 A segunda atividade de elicitação foi a de *benchmarking*. Para tanto, o grupo escolheu realizar o estudo de dois *sites* pertinentes ao contexto geral da aplicação (Reclame Aqui e Consumidor.gov.br) e de uma *feature* específica de um *site* de contexto distinto (Album of the Year).

### **Benchmark**: *Reclame Aqui (reclameaqui.com.br)*

*Site* para reclamações sobre produtos e serviços e pesquisa sobre reputação de empresas.

#### **Documentação de Features e Funcionalidades**

Para esta etapa, seguimos três rotas dentro do *site*: busca de uma empresa, abertura de uma reclamação e comparação entre instituições do mesmo ramo de negócio.

As *features* que se destacaram no processo estão listadas abaixo.

- **Página de empresa**

Cada empresa cadastrada no sistema possui uma página com seu nome (juntamente com uma breve descrição da instituição e informações como CNPJ e contato), sua nota (que pode ser a avaliação geral dada pelo *site* ou referente a um certo período de tempo), número de reclamações (sendo que as queixas mais recentes estão em destaque no centro da tela), número de problemas resolvidos, uma seção com um carrossel com empresas que podem ser de interesse do usuário (baseado na semelhança com a instituição da página atual), um resumo com o tipo de reclamações (qual a queixa mais frequente e qual produto ou serviço apresentou mais problemas).

![Exemplo de página da empresa](https://drive.google.com/uc?id=1yw-U8wffGxQgdjLvjMNYQsoeHRCNm7uV)

![Continuação da página da empresa](https://drive.google.com/uc?id=1QKg_h1ko6zvBFJorI-JK9KKjTLv2RUf4)

*Exemplo de página de empresa.*

- **Barra de busca**

Essa funcionalidade aparece em posição de destaque na página inicial, no centro da parte superior da tela. À medida que o usuário digita sua busca, sugestões de resultados (contendo logo, nome da empresa e nota relativa aos últimos 6 meses) são apresentadas.

![Resultado da busca usando a barra de pesquisa](https://drive.google.com/uc?id=1YcoJ0mFzvrQ8OhbG3uKWHC1O2-9Kdtet)

*Exemplo de busca usando a barra de pesquisa.*

- **Página inicial**

A tela inicial apresenta barra de buscas e uma seção com seis atalhos sendo eles: ferramenta de busca do *site*, formulário de cadastro de empresas, cupons de desconto de instituições diversas, central de ajuda, formulário para reclamações e detector de *site* confiável.

A página possui, ainda, um *ranking* com a classificação das 5 melhores e das 5 piores empresas (as listas podem ser exibidas de acordo com o nicho de atuação das empresas ou segundo a classificação geral, sem distinção por área de atuação).

![Topo da página inicial](https://drive.google.com/uc?id=1A448V_hIx97WRnjQjiH7xalQ_OcxYpj_)

![Continuação da página inicial](https://drive.google.com/uc?id=1tndcLgqIDXu6IeElZJ-B_goDq6cOQMHu)

*Página inicial.*

- **Comparador de empresas**

A página possui uma barra de busca para que o usuário inclua a primeira empresa que deseja adicionar (após a inserção, os outros campos de adição aparecerão com sugestões de empresas do mesmo ramo de negócios que possam interessar ao usuário incluir na comparação). Cada instituição adicionada conta com sua nota referente aos últimos 6 meses, um breve índice sobre o número de reclamações e de problemas solucionados e um resumo com as principais queixas, com cada item contendo direcionamento para as reclamações relacionadas.

![Comparador de empresas](https://drive.google.com/uc?id=1AiiRfuKO_pie-_aujPch0tcJ-cf1gzBL)

*Exemplo de uso do comparador.*

#### **Pontos Positivos e Negativos**

- **Positivos**
    - Features e funcionalidades consideradas mais importantes possuem destaque (como a lista com as últimas reclamações e a barra de busca).
    - Critérios de avaliação usados para calcular a nota e a reputação de cada empresa estão bem esclarecidos aos usuários.
    - As empresas incluídas no comparador possuem informações relevantes e sucintas e links de direcionamento para as seções com reclamações de cada categoria.
- **Negativos**
    - Excesso de informações em algumas páginas. Na tela inicial, por exemplo, a presença da barra de busca em local de destaque torna o botão de “pesquise uma empresa” desnecessário. Já na página da empresa, a possibilidade de ver a nota da instituição referente a quatro períodos de tempo distintos além da nota geral pode tornar a informação confusa para o usuário, sobretudo considerando que a avaliação dos últimos 6 meses é a que configura abaixo dos nomes das empresas sugeridas como resposta a busca do usuário.
    - Apenas três empresas podem ser comparadas simultaneamente.
    - Ao invés da nota geral, o comparador e a ferramenta de busca exibem as notas referentes aos últimos 6 meses.

### **Benchmark**: *consumidor.gov.br*

Um *site* de denúncias e resoluções de problemas relacionados ao consumo, sendo também uma ponte entre clientes e empresas a fim de resolver problemas diversos.

#### **Documentação de Features e Funcionalidades**

Para esta etapa, foi realizado o uso típico da aplicação e foram exploradas funcionalidades de interesse, ou seja, que poderiam ser usadas ou adaptadas na aplicação final do grupo.

As *features* são especificadas mais a fundo a seguir.

- **Acessibilidade**

O *site* apresenta funcionalidades de acessibilidade diversas, incluindo leitores de tela em Libras, várias maneiras de navegação por meio do uso exclusivo do teclado e uma opção de alto contraste de cores.

![Menu de acessibilidade](https://drive.google.com/uc?id=1VT3uPEFRIoNG94vl9hdsZXRmoiByB_n7)

*Exemplo do menu de acessibilidade.*

- **Pesquisa**

O site possui uma barra de busca por empresa (via nome) logo na tela inicial. Conforme o usuário digita o nome da empresa, o *site* fornece sugestões de resultado. Caso uma instituição não seja encontrada no banco de dados, é fornecida a opção de sugerir sua inclusão no banco de dados (conforme documentado abaixo).

![Barra de pesquisa, exibindo sugestões](https://drive.google.com/uc?id=1IJcZs-1BhvxLQBr3sgqCqWxFRVEZTAxK)

*Barra de pesquisa com sugestões.*

- **Formulário de Sugestão de Empresa**

Caso o usuário realize a busca por uma empresa que ainda não está no banco de dados, é possível solicitar sua inclusão no sistema, seja como usuário ou como representante de uma instituição, apenas com uma mudança no processo.

Se for um usuário sugerindo a adição, deve-se preencher um formulário pequeno, listando apenas o nome e o CNPJ da empresa. Só é possível preencher o formulário de o usuário estiver logado.

![Formulário de sugestão de empresa](https://drive.google.com/uc?id=1qGDiYE1j7pyco8COungSjtImopfeg6Ke)

*Formulário de cadastramento de empresa no caso de usuários.*

Se for uma empresa solicitando a parceria, ela preenche um formulário muito mais detalhado, conforme pode ser visto [aqui](https://consumidor.gov.br/pages/credenciada/aderir).

- **Página da Empresa**

Cada empresa registrada no *site* possui uma página própria, a qual apresenta dados de diversas métricas coletadas, como índice de solução de problemas e prazo médio das respostas dadas pela empresa aos clientes que reclamam. Há também um botão para enviar uma nova reclamação para aquela empresa, além de um outro que retorna o usuário à tela inicial para iniciar outra busca. É possível mudar o tempo usado para coletar as métricas, podendo-se alterar pelas reclamações dos últimos 30 dias, dos últimos 6 meses, do ano todo ou de todos os anos.

![Página com perfil de uma empresa](https://drive.google.com/uc?id=1QzGRba6N3MRZ3UXvGdpyyhdihUG5BXJK)

*Página da empresa.*

A página da empresa não lista as reclamações individuais, as quais estão disponíveis em outra página.

- **Formulário de Reclamação**

O *site* oferece a opção para clientes reclamarem direta e publicamente para empresas sobre uma miríade de problemas. Para tanto, eles devem preencher um formulário de reclamação. O formulário pede diversas informações, como nome da empresa, se a empresa colaborou com a solução do problema, a área de atuação da empresa, o assunto geral e uma descrição do problema. O formulário oferece a opção de preenchimento da descrição usando modelos já definidos. Assim como o formulário de sugestão de empresa, só é possível preencher o formulário de o usuário estiver logado e tiver uma conta nível Prata ou Ouro.

![Formulário para cadastro de reclamação](https://drive.google.com/uc?id=1COAAgin9yxXvfwEfO7rt38478EDMtIvN)

*Formulário de reclamação.*

![Continuação do formulário de reclamação](https://drive.google.com/uc?id=1uo5XPqauo3QymCvivRC299ktmhMzPm0z)

*Seção de descrição da reclamação.*

- **Explorador**

O *site* possui um explorador de empresas participantes, que faz a divisão de empresas cadastradas por área de atuação, com menus que podem ser expandidos para mostrar todas as empresas de um dado ramo. O explorador pode ser visto [aqui](https://consumidor.gov.br/pages/principal/empresas-participantes).

![Explorador de empresas cadastradas no sistema](https://drive.google.com/uc?id=18VHoG4HzD-JwxFa7aOe_4HYJXnjqtttc)

*Explorador de empresas participantes.*

- **Rankings**

O *site* oferece diversos *rankings* sobre empresas considerando diversos aspectos abordados em outras áreas do *site*, como as métricas de denúncias. Os *rankings* podem ser vistos [aqui](https://consumidor.gov.br/pages/indicador/geral/abrir).

![Rankings de empresas para diferentes métricas](https://drive.google.com/uc?id=14sFQXTtMzJXGEMUcIOZtSVbZc75E4so_)

*Rankings de empresas para diferentes métricas.*

- **Página Principal**

A página inicial detalha diferentes funcionalidades disponíveis no *site*, as quais podem ser acessadas diretamente, e também indica um passo a passo do uso ideal da ferramenta.

A página explica o mínimo necessário para se utilizar as ferramentas do site de maneira adequada, como opções de *login* e detalhes sobre o que pode ser consultado. Ela também apresenta vários *links* para páginas que explicam melhor o funcionamento de cada aspecto para os que precisarem de mais informações.

![Seção da página inicial do site, contendo *links* para as diferentes informações fornecidas pelo *site*](https://drive.google.com/uc?id=1yZwvTsrOyKk7uhulzEGUqKgNsReVzjMi)

*Seção da página inicial do site.*

Ademais, todas as principais funcionalidades do *site* podem ser acessadas diretamente por botões na página principal, de modo que ela também configura uma maneira fácil de navegação.

#### **Pontos Positivos e Negativos**

- **Positivos**
    - Opções de acessibilidade amplas e fáceis de usar.
    - Página inicial intuitiva.
    - Os formulários são claros, bem explicados e completos.
    - Pesquisa robusta para a maioria dos casos, fornecendo sugestões em tempo real.
- **Negativos**
    - É necessário digitar corretamente o nome da empresa para realizar a busca (o sistema não busca por nomes similares).
    - Não há barra de pesquisa em cada página, sendo necessário voltar para a página inicial.
    - Página da empresa sem grandes detalhes e informações, de modo que para consultar todas as reclamações é necessário acessar a base de dados em outra página.

### **Benchmark**: *Album of the Year (albumoftheyear.org)*

Ao procurar referências para o sistema de avaliação das empresas, nos deparamos com um *site* de *review* musical chamado Album of the Year (AOTY), o qual possui um exemplo de dupla avaliação pela qual estamos interessados.

- **Avaliação**

O *site* oferece um sistema de avaliação dividido entre nota de críticos de música (enviados por *sites* credenciados) e nota dos usuários do próprio *site*.

![Exemplo mostrando as duas notas de um álbum](https://drive.google.com/uc?id=1sIyhwdhU3cK-P4Aqejd6R4MaUyAv52ts)

*Exemplo de dupla avaliação.*

O *site* também indica o número de avaliações e o ranqueamento do álbum no ano em que foi lançado. A cor da barra também muda de cor dependendo da nota, ficando mais avermelhada no caso de uma pior nota.

Pode-se listar como um ponto positivo a exposição clara das avaliações, podendo ser divididas em uma avaliação profissional e uma mais pessoal dos usuários.

### Requisitos

Com base nos pontos positivos e negativos e cada aplicação estudada, podemos expor uma série de requisitos obtidos pelas análises.

**Nota:** Se um ponto for semelhante a um requisito já citado neste documento, ele foi omitido.

- O sistema deve dar ênfase em funcionalidades consideradas principais, colocando-as em posições de destaque e fácil acesso.
- O sistema deve fornecer explicações claras sobre os métodos avaliativos empregados para a composição de notas de empresas.
- O sistema deve prover opções de acessibilidade para seus usuários.
- O sistema de busca deve prover sugestões de resultados que correspondam parcialmente aos termos de pesquisa, mesmo que estejam incompletos.
