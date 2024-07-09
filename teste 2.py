import requests
from faker import Faker
import json

fake = Faker('pt_BR') #traduzir o faker para portugues

def criar_persona() -> dict: #criei um dicionario com os fakes 
    data = {
        "username" : fake.user_name(),
        "email" : fake.email(),
        "password" : fake.password(),
        "phone" : fake.phone_number(),
        "address" : fake.address(),
        "cpf" : fake.cpf()
        }
    return data

def salvar_json(arquivo_json: str, conteudo: str): #criar duas variaveis temporarias 
    with open(arquivo_json, 'w') as arquivo: #abrir com arquivo_json na escrita 'w' e salvar em arquivo
        arquivo.write(conteudo + '\n') #o que esta na variavela arquivo vai ser escrita na variavel conteudo com quebra de linha
    print('Dados salvo em {}.'.format(arquivo_json))

def criar_user_api(usuario) -> bool:
    endpoint_criar_user = "https://desafiopython.jogajuntoinstituto.org/api/users/"
    resposta = requests.post(endpoint_criar_user, json=usuario)

    if resposta.status.code == 201:
        print('usuario criado com sucesso')

    else:
        print('falha em criar usuario')  