from faker import Faker
import requests

Faker = Faker('pt_BR')

def create_persona() -> dict:
    username = Faker.name().replace(' ', '')
    data = {
        'username': username,
        'email': Faker.email(),
        'password': Faker.password(),
        'phone': Faker.phone_number(),
        'address': Faker.address(),
        'cpf': Faker.cpf()
    }
    return data

def criar_user_api(persona):
    url = 'https://desafiopython.jogajuntoinstituto.org/api/users/'
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, json=persona)
    if response.status_code >= 200 and response.status_code < 300:
        print('Usuário criado com sucesso!')
        return True
    else:
        print(f'Falha ao criar usuário. Status code: {response.status_code}')
        return False

def login_user_api(persona):
    endpoint_login = 'http://desafiopython.jogajuntoinstituto.org/api/users/login/'
    login_data = {
        'email': persona['email'],
        'password': persona['password']
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(endpoint_login, headers=headers, json=login_data)
    if response.status_code == 200:
        print('Login realizado com sucesso!')
    else:
        print(f'Falha ao realizar login. Status code: {response.status_code}')

# Criar uma persona
usuario = create_persona()
print('Dados da Persona:', usuario)

# Criar usuário usando a API
if criar_user_api(usuario):
    # Realizar login usando a API
    login_user_api(usuario)
