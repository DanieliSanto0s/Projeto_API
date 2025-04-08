# API de Usuários com Flask e MySQL

Este projeto consiste em uma API REST desenvolvida em **Python** utilizando o framework **Flask**, conectada a um banco de dados **MySQL**, que permite realizar operações CRUD na tabela `usuarios`. O projeto foi desenvolvido como parte da disciplina de Programação Multiplataforma do curso de Análise e Desenvolvimento de Sistemas.

---

## Funcionalidades Disponíveis

- **Listar usuários**: `GET /usuarios`
- **Buscar usuário por ID**: `GET /usuarios/<id>`
- **Criar novo usuário**: `POST /usuarios`
- **Atualizar usuário existente**: `PUT /usuarios/<id>`
- **Deletar usuário**: `DELETE /usuarios/<id>`
- **Autenticar usuário**: `POST /usuarios/auth`

---

## Estrutura do Projeto

```
Projeto_API/
├── database.py          # Arquivo de conexão com o banco de dados MySQL
├── server.py            # Arquivo principal contendo as rotas da API
├── usuarios.py          # Arquivo com as funções de CRUD e autenticação
└── usuarios.sql         # Script SQL para criação da base de dados e inserção de dados iniciais
```

---

## Tecnologias Utilizadas

- Python 3.12+
- Flask
- SQLAlchemy
- MySQL (via XAMPP)
- Postman (para testes das rotas)

---

## Como Executar o Projeto

1. Inicie o servidor MySQL utilizando o XAMPP.
2. Importe o arquivo `usuarios.sql` no phpMyAdmin para criar o banco de dados `projeto` e a tabela `usuarios`.
3. Instale as dependências necessárias:

```bash
pip install flask sqlalchemy mysql-connector-python
```

4. Execute o servidor Flask:

```bash
python server.py
```

5. Acesse as rotas da API através do Postman ou navegador em:

```
http://127.0.0.1:5000
```

---

## Autora

**Danieli Santos**  
Curso: Análise e Desenvolvimento de Sistemas  
Disciplina: Programação Multiplataforma

---

> Este projeto foi desenvolvido com foco educacional e acadêmico, com o objetivo de aplicar conceitos práticos de desenvolvimento web e integração com banco de dados relacional.

