import requests
import json

#---------------------- Lógica principal ----------------------#
def main():
    client_id = 'c55d1f24-6847-4dc7-8a6c-de3e672116ce_6b4c3b8d-4cfe-44b3-9b8e-98e61a390a77'  # ID do cliente
    client_secret = 'g0U4Z0Y8hb3DIzMK/aUjuoDovRNC4H05WRt75BWOZtQ='  # segredo do cliente
    
    # Obter o token de acesso
    token = get_access_token(client_id, client_secret)
    
    # Solicitar ao usuário o código da doença
    disease_code = input("Entre o código da doença: ").strip()
    
    try:
        # Obter informações da doença
        disease_info = get_disease_info(disease_code, token)
        
        # Salvar as informações em um arquivo JSON
        save_to_json(disease_info, f'disease_info_{disease_code}.json')
        
        print(f"As informações para o código da doença '{disease_code}' foram salvas em 'disease_info_{disease_code}.json'")
    except requests.exceptions.HTTPError as e:
        print(f"Erro ao buscar dados para o código {disease_code}: {e}")

#---------------------- Funções ----------------------#
# Função para obter o token OAuth2
def get_access_token(client_id, client_secret):
    token_endpoint = 'https://icdaccessmanagement.who.int/connect/token'
    scope = 'icdapi_access'
    grant_type = 'client_credentials'
    
    # Definir dados para enviar
    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': scope,
        'grant_type': grant_type
    }
    
    # Fazer a requisição
    response = requests.post(token_endpoint, data=payload, verify=False)
    response.raise_for_status()  # Levantar um erro para respostas ruins
    return response.json()['access_token']

# Função para obter informações da doença da API ICD
def get_disease_info(disease_code, token):
    uri = f'https://id.who.int/icd/entity/{disease_code}'  # Usar disease_code na URI

    # Campos de cabeçalho HTTP a serem definidos
    headers = {
        'Authorization': 'Bearer ' + token,
        'Accept': 'application/json',
        'Accept-Language': 'pt',  # Alterado para português
        'API-Version': 'v2'
    }
    
    # Fazer a requisição
    response = requests.get(uri, headers=headers, verify=False)
    response.raise_for_status()  # Levantar um erro para respostas ruins
    return response.json()

# Função para salvar dados em arquivo JSON
def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)  # Escrever dados com indentação para legibilidade

if __name__ == "__main__":
    main()
