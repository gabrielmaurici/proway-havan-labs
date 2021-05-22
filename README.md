# Casa de Câmbio Muito Dinheiro

#### Do que se trata o programa?

É um sistema para que o funcionário de uma empresa que faz transações de câmbio converta , cadastre e análise as transações de um cliente.

A cada transação feita é cobrado uma taxa de 10% sobre o valor, o funcionário terá acesso ao valor desta taxa também.

#### Como funciona?

O funcionário terá 3 opções no menu inicial:

<img src = "/fotos-readme/menu-principal.png" style = "float: left">

###### Ao entrar na 1ª opção do menu principal o funcionário ira cadastrar dados como:

- Nome do cliente
- Data da transação
- Moeda de origem 
- Valor da moeda de origem
- Moeda de destino
- Cotação da moeda de destino em relação a moeda de origem
- E caso a moeda de destino não seja o REAL, ira pedir a cotação do real em relação a moeda de destino

Após seguir todo processo, o funcionário terá a confirmação da transação feita com o valor da conversão e com o valor da taxa de 10% já convertido para real cobrada em cima do cliente:

<img src = "/fotos-readme/transacao-concluida.png" style = "float: left">

###### Ao entrar na 2ª opção do menu principal, o funcionário receberá um menu com as opções para busca de dados:

<img src = "/fotos-readme/menu-relatorios.png" style = "float: left">

Na 1ª opção, o funcionário poderá buscar os dados de um cliente específico, o relatório trará todas as transações deste mesmo cliente pesquisado, contendo os dados cadastrados de cada transação, incluindo mais uma informação de taxa total, que será calculado a soma de todas as taxas cobradas sob este cliente.

<img src = "/fotos-readme/relatorio-cliente.png" style = "float: left">

Na 2ª opção, o funcionário poderá buscar os dados por intervalos de datas, por exemplo, transações feitas do dia 15/05/2021 ao dia 18/05/2021. Segue o mesmo padrão da busca de dados por nome de cliente, porém, ao invés de mostrar a taxa total de cada cliente, irá mostrar a taxa total de todas as transações referente ao intervalo de data escolhido pelo funcionário.

<img src = "/fotos-readme/relatorio-datas.png" style = "float: left">

Na 3ª opção, o funcionário poderá buscar todas as transações já realizadas, seguindo o padrão das outras buscas, a diferença neste caso, é que irá somar o total de taxas de todas as transações do sistema.

<img src = "/fotos-readme/relatorio-sistema.png" style = "float: left">



# Documentação Técnica

#### Sistema de Conversão e Cadastro de Transações

A conversão dos câmbios e os cadastros das transações acontecem simultaneamente. A partir do momento em que o funcionário entra na opção 'Nova Transação de Moedas' é pedido as informações para realizar o cadastro e também a conversão das moedas, todos os inputs do funcionário e saídas de dados como valor da conversão e da taxa são armazenados em variáveis que são chamadas para dentro de um dicionário ao fim da conversão.

<img src = "/fotos-readme/dicionario.png">

#### Armazenamento dos Dados

Para o armazenamento de dados, foi usado como 'banco de dados' um arquivo txt em binário, onde é armazenada em uma lista de dicionário todas as transações, cada dicionário recebe os dados de uma transação executada pelo funcionário como explicado no tópico a cima, e a lista recebe esses dicionários.

Para fazer este 'banco de dados', foi criado um arquivo python 'criar-arquivo-binario.py' separadamente do projeto principal, onde foi importado o método pickle para gravar uma imagem com a lista 'transacoes' que recebe os dicionários.

<img src = "/fotos-readme/criacao-arquivotxt.png"> 

Após o processo de conversão e cadastro o dicionário fica com os dados da transação temporariamente salvo, para passar a transação para dentro do 'banco de dados' é preciso abrir o arquivo 'transacoes.txt' com o método 'rb' para poder adicionar dados em binário e também receber os dados já dentro desse arquivo numa lista temporária 'transacoes', que como mostra a imagem a baixo, foi setada antes de abrir o arquivo

<img src = "/fotos-readme/append.png" style = "float: left">

Após a lista 'transacoes' receber os dados do arquivo 'transacoes.txt', é usada a função 'append' para inserir o dicionário que contem a nova transação ao fim da lista 'transacoes'.

Em seguida o arquivo é aberto novamente, mas dessa vez, com o método 'wb' para poder salvar os dados atualizados por cima dos dados antigos.

#### Leitura dos Dados

Como já explicado, a leitura de dados foi feita de 3 formas diferentes, através do nome do cliente, intervalos de datas e lista completa do sistema. O conceito é basicamente o mesmo nas 3 formas, começando pela busca pelo nome

###### Leitura de dados por nome de Cliente

É feito um input pedindo o nome do cliente, com isso, foi feito um for para ler toda a lista de dicionários, dentro do for foi feita uma condição, onde, se o campo 'cliente' do dicionário for igual ao input do funcionário, irá imprimir todos os dados desse dicionário. Como a condição está dentro de um for, cada vez que o nome for igual ao do dicionário, irá ser imprimido novamente.

Caso o nome do input não estiver dentro de algum dicionário da lista, será impresso a frase 'Não existem transações com este nome'.

<img src = "/fotos-readme/leitura-cliente.png">

###### Leitura de Dados por Intervalos de Datas

Assim como a leitura por nome de cliente, o mesmo acontece por intervalos de datas, a diferença neste caso, é que é preciso fazer com que a data do input do funcionário seja convertida para o padrão 'Ano/mês/dia' e transformada em número inteiro, pois não tem como fazer comparações com operadores lógicos usando string. 

Após a comparação a data é formatada novamente para o padrão 'dia/mês/Ano', para que fique mais confortável para o usuário ler. (As funções de formatação estão no início do código e são chamadas quando necessárias)

<img src = "/fotos-readme/leitura-datas.png">

###### Leitura de Dados completa do Sistema

Está leitura, diferente das outras, não precisa de condições, como a ideia é mostrar todas as transações do sistema, basta um for imprimindo todos os dicionários da lista.

<img src = "/fotos-readme/leitura-geral.png">

# Como Executar o Programa

Primeiramente é preciso ter instalado o Python na sua máquina.

Link para download: https://www.python.org/downloads/release/python-395/

Após ter instalado o Python, é preciso ter no mesmo diretório os arquivos 'calculadora.py' e 'transacoes.txt' para que você consiga puxar os dados já armazenados, ou , para que consiga armazenar mais dados. 

O arquivo 'transacoes.txt' já possuí dados para realizar testes, caso queira começar os dados do zero, precisará ter no mesmo diretório 'calculadora.py' e 'criar-arquivo-binario.py'.

<img src = "/fotos-readme/arquivos-compilacao.png" >

Feito isso, é possível executar o programa buscando a pasta em que está armazenado pelo Prompt de Comando (CMD)
