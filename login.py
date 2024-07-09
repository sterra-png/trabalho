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