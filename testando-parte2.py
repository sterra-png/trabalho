import requests
from faker import Faker
import json

fake = Faker('pt_BR')

def criar_persona() -> dict: #estou criando um def com o nome create_persona e estou falando que o conteudo dele e um dicionario
    data = {
        "username" : fake.user_name(),
        "email" : fake.email(),
        "password" : fake.password(),
        "phone" : fake.phone_number(),
        "address" : fake.address(),
        "cpf" : fake.cpf()
    }

    return data 
 
def salvar_json (arquivo_json: str , conteudo: str) : #criei duas variaves temporarias 
    with open (arquivo_json,'w') as arquivo: # abrir com a variavel login_json na escrita 'w'e salvar em 'arquivo'
        arquivo.write(conteudo + '\n') #o conteudo de arquivos vai ser escrito na varieval conteudo com a quebra de linha
        print('dados salvos em {}'.format(arquivo_json))

def criar_usuario_api(usuario) -> bool:
    endpoint_criar_usuario = "https://desafiopython.jogajuntoinstituto.org/api/users/" #criar uma variavel que guarda a url do site
    resposta = requests.post(endpoint_criar_usuario , json = usuario) #estou requisitando que o vs code poste no site

if resposta.status_code == 201:
        print('Usuário criado com sucesso!')
        print(resposta.json())
        salvar_json('log_criacao.json', json.dumps(resposta.json(), indent=4))
        return True

else:
        print('Falha ao criar usuário.')
        print('Status code: ', response.status_code)
        print('Resposta: ', response.json())
        salvar_json('log_criacao.json', json.dumps(response.json(), indent=4))
        return False