# Pass Test

Pass_test ou password tester é uma micro aplicação em python para checagem de senhas com regras definidas dinamicamente.

Pass_test utiliza Grapql e Fast Api para receber requisições em HTTP com a senha e as regras a serem definidas e retorna uma boleana com o resultado da analise e uma lista com as regras que não foram seguidas em caso de falha.

As bibliotecas Uvicorn e Strawberry são utilizadas para realizarem a integração entre o Fast Api e o Graphql.

Portanto, as dependências desse projeto são:
- python 
- fastapi 
- uvicorn 
- strawberry-graphql

Além disso são utilizadas as bibliotecas no auxilio do desenvolvimento (group dev):
- pytest: Testes unitários
- isort: Organização dos imports
- mkdocs: Documentação
- blue: Formatação automática
- pytest-cov: Opções para verificação de cobertura dos testes
- pip-audit: Verificação de integridade das bibliotecas utilizadas no projeto

**A versão base do Python desse projeto é a 3.11**

## Para realizar download do projeto:
~~~
git clone https://github.com/MarcoLemos/Pass_test.git
~~~

Nesse projeto foi utilizado a biblioteca poetry para criar o ambiente virtual e arquivo Makefile para organizar e simplificar os comandos.

## Para instalar o Make:

~~~
sudo apt install make
~~~

## Para instalar o poetry:

### Linux ou wsl
~~~
curl -sSL https://install.python-poetry.org | python3 -
~~~

### Powershell
~~~
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
~~~
Instruções adicionais podem ser encontradas na documentação da biblioteca. [Poetry Docs](https://python-poetry.org/docs/)

## Opcional: Se preferir criar o ambiente virtual na pasta raiz do projeto
~~~
poetry config virtualenvs.in-project true
~~~

## Para instalar as dependências 
~~~
make install
~~~

## Inicializar o ambiente virtual

~~~
make shell
~~~

## Uma vez instaladas as dependências, esse documento pode ser visualizado em um servidor local

### Pagina criada com auxilio da biblioteca mkdocs
~~~
make docs
~~~

## **Para rodar o projeto**

~~~
make run
~~~

O projeto estará acessível em (http://0.0.0.0:8000/graphql)

O projeto também conta com dependências para formatação, teste e checagem de bibliotecas

## Para rodar os testes

~~~
make test
~~~

## Para rodar os testes com coverage

~~~
make cover
~~~

## Para executar a formatação 

### Para formatação automática seguindo a pep8 são utilizadas as bibliotecas blue e isort

~~~
make format
~~~

## Checagem das bibliotecas com pip-audit

~~~
make sec
~~~

## Dockerfile

Para criar a imagem
- imagem **passimage**
~~~
make image
~~~

Para criar o container
- container **passcontainer**
- O acesso pode ser feito na porta (http://0.0.0.0:8080/graphql)
~~~
make cont
~~~

## Git hooks

Esse projeto conta com configuração básica de pre commit. São executados os comandos de testes e formatação. 
O hook pode ser encontrado em:

~~~
.git/hooks/pre-commit
~~~

## Github actions

Esse projeto conta com analise integrada do github actions. São executados os comandos de testes e formatação. 
O arquivo de workflow pode ser encontrado em:

~~~
.github/workflows/continuos_integration.yml
~~~
