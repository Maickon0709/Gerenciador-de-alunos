# Gerenciador de Alunos

Sistema simples de gerenciamento de alunos desenvolvido em Python utilizando SQLite para armazenamento de dados.

## Funcionalidades

* Cadastrar alunos
* Listar todos os alunos cadastrados
* Buscar aluno pelo nome
* Atualizar cadastro de alunos
* Excluir alunos do banco de dados

## Tecnologias Utilizadas

* Python 3
* SQLite3

## Estrutura do Projeto

```text
Gerenciador-de-alunos/
│
├── banco.py
├── alunos.py
├── menu.py
├── academia.db
└── README.md
```

## Banco de Dados

A tabela `alunos` possui os seguintes campos:

| Campo | Tipo                |
| ----- | ------------------- |
| id    | INTEGER PRIMARY KEY |
| nome  | TEXT                |
| idade | INTEGER             |
| plano | TEXT                |

## Funcionalidades do Sistema

### Cadastrar Aluno

Permite inserir um novo aluno no banco de dados informando:

* Nome
* Idade
* Plano

### Listar Alunos

Exibe todos os alunos cadastrados no sistema.

### Buscar Aluno

Realiza uma consulta pelo nome do aluno e exibe seus dados.

### Atualizar Cadastro

Permite alterar:

* Nome
* Idade
* Plano

de um aluno existente através do ID.

### Excluir Aluno

Remove um aluno do banco de dados utilizando seu ID.

## Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/Maickon0709/Gerenciador-de-alunos.git
```

2. Acesse a pasta do projeto:

```bash
cd Gerenciador-de-alunos
```

3. Execute o arquivo principal:

```bash
python menu.py
```

## Objetivo do Projeto

Este projeto foi desenvolvido com fins de aprendizado, praticando conceitos de:

* CRUD (Create, Read, Update e Delete)
* Banco de Dados SQLite
* Modularização em Python
* Funções
* Manipulação de dados utilizando SQL

## Autor

Maickon H.
Estudante de Análise e Desenvolvimento de Sistemas.
