# Pass Test

Pass_test ou password tester é uma micro aplicação em python para checagem de senhas com regras definidas dinamicamente.

Pass_test utiliza Grapql e Fast Api para receber requisições em HTTP com a senha e as regras a serem definidas e retorna uma boleana com o resultado da analise e uma lista com as regras que não foram seguidas em caso de falha.

As bibliotecas Uvicorn e Strawberry são utilizadas para realizarem a integração entre o Fast Api e o Graphql.

A versão base do Python desse projeto é a 3.11.1

Para realizar download do projeto
~~~
git clone https://github.com/MarcoLemos/Pass_test.git
~~~

Nesse projeto foi utilizado a biblioteca poetry para criar o ambiente virtual e arquivo Makefile para organizar e simplificar os comandos.

Para instalar o poetry:

~~~
#Linux ou wsl
curl -sSL https://install.python-poetry.org | python3 -
~~~

~~~
#Powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
~~~
Instruções adicionais podem ser encontradas na documentação da biblioteca.

[Poetry Docs](https://python-poetry.org/docs/)

Para instalar as dependências 

~~~
make install
~~~

Inicializar o ambiente virtual

~~~
make shell
~~~

Uma vez instaladas as dependências, esse documento pode 
ser visualizado em um servidor local

~~~
make docs
~~~

E para rodar o projeto

~~~
make run
~~~

O projeto estará acessível em (http://0.0.0.0:8000/graphql)

O projeto também conta com dependências para formatação, teste e checagem de bibliotecas

Para rodar os testes

~~~
make test
~~~

Para rodar os testes com coverage

~~~
make cover
~~~

Para formatação automática seguindo a pep8 são utilizadas as bibliotecas blue e isort

~~~
make format
~~~

Checagem das bibliotecas com pip-audit

~~~
make sec
~~~
