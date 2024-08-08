# SISREG

Sistema de Registro de Documento


## Ferramentas Utilizadas

- `Python 3.12.1`

- `SQLAlchemy 2.0.30`

- `Fastapi 0.111.0`

- `PostgreSQL`

  
## Acessando o repositório

- Você pode clonar o repositório na sua máquina com o comando git clone https://github.com/fesflabs/sisreg.git.

- Para criar um ambiente virtual, use o comando: `python -m venv venv` no terminal e ative o ambiente com o comando: `.\venv\Scripts\activate`

- Com o ambiente ativado, instale as dependências: `pip install -r requirements.txt`

  
## Utilização e criação de token de segurança

Alguns endpoints precisam de autenticação para serem chamados, e para isso é preciso gerar um token de segurança.

- Abra um terminal e execute o comando: `python -c "import secrets; print(secrets.token_urlsafe(32))"`

- Salve esse token na variável JWT_SECRET no arquivo configs.py

  
## Banco de Dados

Para armazenar os dados das requisições, é preciso utilizar um banco de dados.
O banco de dados utilizado nesse sistema foi o PostgreSQL.

- Crie um banco de dados PostgreSQL.

- Após a criação do banco, execute o arquivo criar_tabelas.py com o comando: `python criar_tabelas.py`

- Cheque o arquivo configs.py na pasta core para configurar seu ambiente.

  
## Arquivo configs.py

- Na variável `DB_URL`, altere os parâmetros necessarios de acordo com a criação do banco de dados.
  Os parâmetros são, em sequência, seu usuário postgres, sua senha postgres, o local onde vai estar hospedado, e o nome do banco.

- Na variável `JWT_SECRET `, você vai colocar o token gerado anteriormente.



## API/V1

- Diretório de endpoints da API.


## Estrutura de Diretórios e arquivos

- `api/v1/`
  > api.py
  O arquivo api.py é um arquivo de organização para facilitar o acesso entre os diferentes endpoints.

- `api/v1/endpoints/`
  
  > documentos.py
  
  O arquivo documentos.py é o endpoint para gerar o numero de registro dos documentos, além de realizar outras ações.

- `api/v1/endpoints/`
  
  > usuario.py
  
  O arquivo usuario.py é o endpoint voltado ao usuário, utilizado para validação de login e outras ações.

  
## Endpoints

### Documentos

```python

/

```

Essa é a rota raiz, e nela é possível realizar solicitações POST para gerar numeração do documento, e GET para listar todos os documentos.



```python

/{documento_id}

```

Essa é a rota direcionada ao documento pelo ID, nela é possível realizar solicitações de GET para ver os dados daquele documento, solicitações PUT para atualizar o documento, e solicitações de DELETE para deletar documentos