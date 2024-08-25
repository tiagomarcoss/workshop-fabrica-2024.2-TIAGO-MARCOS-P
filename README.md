# Meu Projeto Django
 Este é um projeto Django simples que implementa um 
conversor de moedas usando uma API de taxas de 
câmbio.
 ## Requisitos- Python 3.x- Django 3.x ou superior- `requests` library
 ## Instalação
 1. Clone o repositório para sua máquina local:
    ```bash
    git clone https://github.com/tiagomarcoss/workshop-fabrica-2024.2-TIAGO-MARCOS-P
    projeto-django.git
    cd meu-projeto-django
    ```
 2. Crie e ative um ambiente virtual:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows: 
    venv\Scripts\activate
    ```
 3. Instale as dependências do projeto:
    ```bash
    pip install -r requirements.txt
    ```
 4. Altere os dados do Banco para o seu Banco:
```bash
 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': ‘(nome do seu banco, padrão: banco), 
        'USER': 'postgres',
        'PASSWORD': ‘(senha do SEU postgresql)‘,
        'HOST': 'localhost',  
        'PORT': '5432',        
    }
 }
 ```
 5. Configure o banco de dados:
    ```bash
    python manage.py migrate
    ```
 6. Crie um superusuário para acessar o admin do 
Django:
    ```bash
    python manage.py createsuperuser
    ```
 7. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```
 ## Como usar
 ```
 Ao acessar a rota inicial você vai poder criar o seu 
 usuário, após a criação poderá cadastrar a sua conta 
 bancaria, com ela feita poderá ser feito a leitura de seu 
 saldo em suas diferentes carteiras, fazer atualizações 
 nela e cancelar a sua conta bancaria. 
 Todos as rotas terão botões de redirecionamento para 
 as etapas sequenciais.
 ```
