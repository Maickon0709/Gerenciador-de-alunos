# Gerenciador de Alunos

Sistema simples de gerenciamento de alunos desenvolvido em Python com MySQL para armazenamento de dados.

## Funcionalidades

- Cadastrar alunos
- Listar todos os alunos cadastrados
- Buscar aluno pelo nome
- Atualizar cadastro de alunos
- Excluir alunos do banco de dados

## Tecnologias Utilizadas

- Python 3
- MySQL 8.0
- mysql-connector-python
- python-dotenv

## Estrutura do Projeto
Gerenciador de alunos/ │ ├── banco.py ├── alunos.py ├── main.py ├── .env ← não sobe pro GitHub (contém credenciais) ├── .gitignore └── README.md

## Banco de Dados

A tabela `alunos` possui os seguintes campos:

| Campo | Tipo         |
|-------|--------------|
| id    | INT (PK, AI) |
| nome  | VARCHAR(50)  |
| idade | TINYINT      |

## Como Executar

1. Clone o repositório:
git clone https://github.com/Maickon0709/Gerenciador-de-alunos.git

2. Instale as dependências:
pip install mysql-connector-python python-dotenv

3. Crie o arquivo `.env` na raiz do projeto:
DB_HOST=localhost DB_USER=root DB_PASSWORD=sua_senha DB_NAME=gerenciador_alunos

4. Execute:
python main.py

## Autor

Maickon H. — Estudante de Análise e Desenvolvimento de Sistemas.
