import requests
from faker import Faker
import json

fake = Faker('pt_BR')

def criar_persona() -> dict: #estou criando um def com o nome criar_persona e estou falando que o conteudo dele e um dicionario
    data = {
        "username": fake.user_name(),
        "email": fake.email(),
        "password": fake.password(),
        "phone": fake.phone_number(),
        "address": fake.address(),
        "cpf": fake.cpf()
    }
    return data

usuario = criar_persona
print(usuario)

def salvar_json(arquivo_json: str, conteudo: str):
    with open(arquivo_json, 'w') as arquivo:
        arquivo.write(conteudo + '\n')
        print('Dados salvos em {}'.format(arquivo_json))

def criar_usuario_api() -> bool:
    endpoint_criar_usuario = "https://desafiopython.jogajuntoinstituto.org/api/users/"
    resposta = requests.post(endpoint_criar_usuario, json=usuario)

    if resposta.status_code == 201:
        print('Usuário criado com sucesso!')
        print(resposta.json())
        salvar_json('log_criacao.json', json.dumps(resposta.json(), indent=4))
        return True
    else:
        print('Falha ao criar usuário.')
        print('Status code: ', resposta.status_code)
        print('Resposta: ', resposta.json())
        salvar_json('log_criacao.json', json.dumps(resposta.json(), indent=4))
        return False
