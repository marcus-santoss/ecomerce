# eCommerce

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
python manage.py runserver
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