import requests
from faker import Faker
import json

fake = Faker('pt_BR')  # Traduzir o faker para português

def criar_persona() -> dict:
    # Criar um dicionário com dados falsos
    data = {
        "username": fake.user_name(),
        "email": fake.email(),
        "password": fake.password(),
        "phone": fake.phone_number(),
        "address": fake.address(),
        "cpf": fake.cpf()
    }
    print(f'Dados do usuário gerados: {data}')  # Mensagem de depuração
    return data

def salvar_json(arquivo_json: str, conteudo: dict):
    # Salvar conteúdo JSON em um arquivo
    with open(arquivo_json, 'w') as arquivo:
        json.dump(conteudo, arquivo, ensure_ascii=False, indent=4)
    print(f'Dados salvos em {arquivo_json}.')  # Mensagem de depuração

def criar_user_api(usuario) -> bool:
    endpoint_criar_user = "https://desafiopython.jogajuntoinstituto.org/api/users/"
    print(f'Enviando solicitação para criar usuário: {usuario}')  # Mensagem de depuração
    resposta = requests.post(endpoint_criar_user, json=usuario)

    print(f'Resposta do servidor: {resposta.status_code} {resposta.text}')  # Mensagem de depuração

    if resposta.status_code == 201:
        print('Usuário criado com sucesso!')
        return True
    else:
        print('Falha ao criar usuário')
        print('Status Code:', resposta.status_code)
        print('Resposta:', resposta.json())
        return False

def login_user_api(usuario) -> dict:
    endpoint_login_user = "http://desafiopython.jogajuntoinstituto.org/api/users/login/"
    login_data = {
        "username": usuario["username"],
        "password": usuario["password"]
    }
    print(f'Enviando solicitação de login: {login_data}')  # Mensagem de depuração
    resposta = requests.post(endpoint_login_user, json=login_data)

    print(f'Resposta do servidor: {resposta.status_code} {resposta.text}')  # Mensagem de depuração

    if resposta.status_code == 200:
        print('Login realizado com sucesso!')
        return resposta.json()
    else:
        print('Falha ao fazer login')
        print('Status Code:', resposta.status_code)
        print('Resposta:', resposta.json())
        return None

if __name__ == "__main__":
    usuario = criar_persona()
    
    if criar_user_api(usuario):
        login_response = login_user_api(usuario)
        if login_response:
            salvar_json('login_response.json', login_response)
