# Projeto de Livraria Online — Atividade Prática

## Descrição

Este projeto é uma livraria online construída com Flask e MongoDB Atlas.  
**Sua principal tarefa é implementar os métodos do arquivo `models.py`, que atualmente estão vazios (`pass`).**

Você deverá:

- Instalar as dependências do projeto.
- Configurar o arquivo `.env` com sua URI do MongoDB Atlas.
- Testar a conexão com o banco de dados.
- Popular o banco de dados com os dados iniciais.
- Implementar os métodos do `models.py` para manipulação dos dados.

## Passos para Realizar a Atividade

### 1. Instale os requisitos do projeto

Abra o terminal na pasta do projeto e execute:

```bash
pip install -r requirements.txt
```

### 2. Configure o arquivo `.env`

Crie um arquivo chamado `.env` na raiz do projeto com o seguinte conteúdo (ajuste para sua conexão):

```
MONGO_URI=mongodb+srv://:@.mongodb.net/?retryWrites=true&w=majority
```

Substitua ``, ``, `` e `` pelos seus dados do MongoDB Atlas.

### 3. Teste a conexão com o MongoDB

Execute o script de teste de conexão para garantir que sua URI está correta e o banco está acessível:

```bash
python teste_conexao_mongodb.py
```

Se a conexão for bem-sucedida, você verá uma mensagem de sucesso no terminal.

### 4. Popule o banco de dados

Execute o script de popular o banco, que está na pasta `banco`:

```bash
python banco/popula_banco.py
```

Esse script irá inserir os dados iniciais no seu banco MongoDB Atlas.

### 5. Implemente os métodos do `models.py`

Abra o arquivo `models.py`.  
Você encontrará métodos apenas com `pass`.  
Implemente cada método utilizando PyMongo para acessar e manipular os dados do MongoDB.

**Exemplos de métodos a serem implementados:**

- Buscar livros com filtros e paginação.
- Buscar livro por ID.
- Obter categorias e tags disponíveis.

**Dicas:**
- Use o tipo `Decimal128` para campos de preço.
- Trate datas corretamente.
- Mantenha a lógica de acesso ao banco de dados apenas dentro do `models.py`.

## Estrutura do Projeto

- `app.py` — ponto de entrada da aplicação Flask
- `routes.py` — define as rotas da aplicação
- `models.py` — onde você vai implementar a lógica de acesso ao banco
- `templates/` — arquivos HTML (Jinja2)
- `static/` — arquivos CSS e JS
- `.env` — variáveis de ambiente (NÃO compartilhe este arquivo publicamente)
- `banco/popula_banco.py` — script para popular o banco de dados

## Suporte

Se tiver dúvidas, consulte o material da disciplina, a documentação oficial do Flask e do PyMongo, ou entre em contato com o professor.

**Bom trabalho!**