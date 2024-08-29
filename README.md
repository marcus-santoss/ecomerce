# eCommerce

Projeto de avaliação para o cargo de DEV Python.
O Clean Architecture é uma abordagem de design de software que visa
criar sistemas flexíveis, escaláveis e de fácil manutenção.
Ele se baseia na separação de responsabilidades e na independência de
frameworks e tecnologias, organizando o código em camadas que isolam a
lógica de negócios das dependências externas. Isso permite que o software
seja mais adaptável a mudanças e teste mais eficazmente.

Este projeto foi criado seguindo este design, utilizando o framework Django
como ferrameta para exposição desta aplicação na Web e Django Rest Framework
para criação de uma API rest.

O banco de dados SQLite3 foi deixado no projeto. Neste banco há tabelas
com os seguintes conteúdos:

- Products: 10 Produtos criados com status de AVAILABLE
- Customer: 2 Usuários criados para realização dos testes das reservas
- Reservations: 2 Reservas já criadas

## Como rodar o projeto

1. **Clone o repositório:**

```shell
git clone <url-do-repositorio>
cd ecommerce
```

2. Crie um ambiente virtual e instale as dependências:

```shell
python -m venv env
source env/bin/activate  # No Windows: env\Scripts\activate
pip install -r requirements.txt
```

3. Aplique as migrações:

```shell
python manage.py makemigrations
python manage.py migrate
```

4. Inicie o servidor:

```shell
python infrastructure/website/manage.py runserver
```

5. Acesse os endpoints:

- Produtos: `/api/products/`
- Reservas do cliente: `/api/customers/{customer_id}/reservations`
- Reservar produto: `/api/products/{product_id}/reserve/`

### List All Products

```http request
GET http://127.0.0.1:8000/api/products/
Content-Type: application/json
```

### List Reserved Products

```http request
GET http://127.0.0.1:8000/api/customer/8/reservations
Content-Type: application/json
```

### Make a Reserve

```http request
POST http://127.0.0.1:8000/api/products/5/reserve/
Content-Type: application/json
```

6. Makefile

Nordway Django

#### Prints help message

```shell
$ make help
```

#### Create new migrations based on models updates

```shell
$ make make-migrations
```

#### Django Manager

```shell
$ make manager
```

#### Apply all migrations in database

```shell
$ make migrate
```

#### Run web sever

```shell
$ make run-server
```
