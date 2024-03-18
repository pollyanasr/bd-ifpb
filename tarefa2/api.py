
import requests

estado = input('Digite a sigla do estado (exemplo: PB para Paraíba):')  
url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{estado}/municipios"
response = requests.get(url)
dados = response.json()

for cidade in dados:
    print(cidade['nome'])

