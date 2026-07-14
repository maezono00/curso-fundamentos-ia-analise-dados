#Importação da biblioteca requests, usada para fazer as requisições em alguma API ou link.
import requests

#O usuário vai inserir o cep e a variável url vai "montar" o link correto do viaCEP para fazer a requisição dos dados inseridos.
cep = input("Digite o seu CEP: ")
url = f"https://viacep.com.br/ws/{cep}/json/"

#Requisição dos dados dentro da variável dados, usando a biblioteca requests com o comando .get(), esses dados serão inseridos numa lista dentro da variável endereco, usando a função .json() na variável dados.
dados = requests.get(url)
endereco = dados.json()

#Print da lista endereço com os itens desejados.
print(f"Você mora na rua {endereco["logradouro"]}, no bairro {endereco["bairro"]} e na cidade {endereco["localidade"]}.")