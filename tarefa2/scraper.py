from bs4 import BeautifulSoup
import requests

url = "https://www.ifpb.edu.br/ppgti/programa/corpo-docente"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
title =  soup.find('h1', class_='documentFirstHeading').string
print(title)
print("")

div = soup.find('div', id='parent-fieldname-text')

docentes = div.find_all('h4')[2:]

for docente in docentes:
    nome = docente.text.replace("\n", "")
    linha_pesquisa = docente.find_next('p').text.replace("\n", "")
    curriculo_lattes = docente.find_next('p').a['href']
    email = docente.find_next('p').find('a', href=True, string=True).text

    print("Nome:", nome)
    print(linha_pesquisa)
    print("Currículo Lattes:", curriculo_lattes)
    print("E-mail:", email)
    print()
