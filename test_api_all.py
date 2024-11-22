#Testes para SpaceX API
#Testar Resposta de Sucesso: Verificar se a API retorna um código de status 200 quando a requisição é feita corretamente.
#Testar Resposta de Erro: Validar a resposta de erro para um lançamento inexistente, garantindo que a API retorne um status 404.
#Verificar Dados do Lançamento: Verificar se os dados de um lançamento (como nome e data) estão corretos.
#Verificar Estrutura de Dados: Validar se a resposta possui as chaves necessárias, como name e flight_number.
#Testar Histórico de Lançamentos: Garantir que a API retorne um histórico de lançamentos com pelo menos um lançamento.

#Código dos Testes

import requests
import pytest

# Fixture para configurar a URL da API
@pytest.fixture
def spacex_api_url():
    return "https://api.spacexdata.com/v4/launches/latest"

# Teste 1: Verificar se a API retorna o status correto (200)
def test_spacex_api_success(spacex_api_url):
    response = requests.get(spacex_api_url)
    assert response.status_code == 200, f"Status code {response.status_code} inesperado"

# Teste 2: Testar resposta de erro para lançamento inexistente
def test_spacex_api_invalid_launch():
    response = requests.get("https://api.spacexdata.com/v4/launches/invalid")
    assert response.status_code == 404, "Lançamento inexistente deve retornar 404"

# Teste 3: Verificar se os dados do lançamento estão corretos
def test_spacex_launch_data(spacex_api_url):
    response = requests.get(spacex_api_url)
    assert response.status_code == 200, f"Status inesperado: {response.status_code}"
    data = response.json()
    assert 'flight_number' in data, "Chave 'flight_number' não encontrada"
    assert 'name' in data, "Chave 'name' não encontrada"
    assert 'date_utc' in data, "Chave 'date_utc' não encontrada"

# Teste 4: Verificar estrutura dos dados de lançamento
def test_spacex_launch_structure(spacex_api_url):
    response = requests.get(spacex_api_url)
    data = response.json()
    assert 'name' in data, "Chave 'name' não encontrada no JSON retornado"
    assert 'name' in data and isinstance(data['name'], str), "Nome do lançamento inválido"

# Teste 5: Testar se a API retorna um histórico de lançamentos
def test_spacex_launch_history():
    response = requests.get("https://api.spacexdata.com/v4/launches")
    data = response.json()
    assert len(data) > 0, "Histórico de lançamentos vazio"


#Testes para PokeAPI
#Testar Resposta de Sucesso: Verificar se a API retorna um código de status 200.
#Testar Resposta de Erro: Validar se a API retorna um erro quando um Pokémon inexistente é solicitado.
#Verificar Dados do Pokémon: Verificar se os dados retornados são corretos, como o nome e o ID do Pokémon.
#Verificar Estrutura dos Dados: Validar a presença de chaves como name, id e types.
#Testar Lista de Pokémon: Garantir que a lista de Pokémon contém pelo menos um Pokémon.

#Código dos Testes

import requests
import pytest

# Fixture para configurar a URL da API
@pytest.fixture
def pokeapi_url():
    return "https://pokeapi.co/api/v2/pokemon/pikachu"

# Teste 1: Verificar se a API retorna o status correto (200)
def test_pokeapi_success(pokeapi_url):
    response = requests.get(pokeapi_url)
    assert response.status_code == 200, f"Status code {response.status_code} inesperado"

# Teste 2: Testar resposta de erro para Pokémon inexistente
def test_pokeapi_invalid_pokemon():
    response = requests.get("https://pokeapi.co/api/v2/pokemon/invalidpokemon")
    assert response.status_code == 404, "Pokémon inexistente deve retornar 404"

# Teste 3: Verificar se os dados do Pokémon estão corretos
def test_pokeapi_pokemon_data(pokeapi_url):
    response = requests.get(pokeapi_url)
    data = response.json()
    assert 'name' in data and data['name'] == 'pikachu', "Nome do Pokémon incorreto"
    assert 'id' in data and data['id'] == 25, "ID do Pokémon incorreto"

# Teste 4: Verificar a estrutura dos dados de Pokémon
def test_pokeapi_pokemon_structure(pokeapi_url):
    response = requests.get(pokeapi_url)
    data = response.json()
    assert 'types' in data, "Chave 'types' não encontrada"

# Teste 5: Verificar lista de Pokémon
def test_pokeapi_pokemon_list():
    response = requests.get("https://pokeapi.co/api/v2/pokemon")
    data = response.json()
    assert len(data['results']) > 0, "Lista de Pokémon vazia"


#Cat Facts API
#A Cat Facts API fornece curiosidades sobre gatos. Vamos escrever 5 testes para ela.

#Testes para Cat Facts API
#Testar Resposta de Sucesso: Verificar se a resposta da API retorna status code 200.
#Testar Resposta de Erro: Validar a resposta para uma requisição inválida.
#Verificar Estrutura de Dados: Confirmar se a resposta contém a chave fact.
#Testar Fato Aleatório: Garantir que o fato retornado seja uma string não vazia.
#Testar Lista de Fatos: Validar se a lista de fatos contém ao menos um fato.

import requests
import pytest

# Fixture para configurar a URL da API
@pytest.fixture
def cat_facts_api_url():
    return "https://catfact.ninja/fact"

# Teste 1: Verificar se a API retorna o status correto (200)
def test_cat_facts_success(cat_facts_api_url):
    response = requests.get(cat_facts_api_url)
    assert response.status_code == 200, f"Status code {response.status_code} inesperado"

# Teste 2: Testar resposta de erro para URL incorreta
def test_cat_facts_invalid_url():
    response = requests.get("https://catfact.ninja/invalid")
    assert response.status_code != 200, "A URL inválida deve retornar erro"

# Teste 3: Verificar se a chave 'fact' está presente na resposta
def test_cat_facts_data_structure(cat_facts_api_url):
    response = requests.get(cat_facts_api_url)
    data = response.json()
    assert 'fact' in data, "A chave 'fact' não está presente na resposta"

# Teste 4: Testar que o fato retornado não está vazio
def test_cat_facts_non_empty(cat_facts_api_url):
    response = requests.get(cat_facts_api_url)
    data = response.json()
    assert len(data['fact']) > 0, "O fato retornado está vazio"

# Teste 5: Validar se a lista de fatos contém ao menos um fato
def test_cat_facts_list():
    response = requests.get("https://catfact.ninja/facts")
    data = response.json()
    assert len(data['data']) > 0, "A lista de fatos está vazia"

#CoinGecko API
#A CoinGecko API fornece dados sobre criptomoedas. Aqui estão os testes.

#Testes para CoinGecko API
#Testar Resposta de Sucesso: Verificar se a resposta da API retorna status code 200.
#Testar Resposta de Erro: Validar a resposta para uma criptomoeda inexistente.
#Verificar Dados da Criptomoeda: Verificar se os dados de uma criptomoeda estão corretos.
#Verificar a Estrutura de Dados: Validar se a resposta contém as chaves id, symbol e name.
#Testar Histórico de Preços: Validar se a API retorna preços históricos.

import requests
import pytest

# Fixture para configurar a URL da API
@pytest.fixture
def coin_gecko_api_url():
    return "https://api.coingecko.com/api/v3/coins/bitcoin"

# Teste 1: Verificar se a API retorna o status correto (200)
def test_coin_gecko_success(coin_gecko_api_url):
    response = requests.get(coin_gecko_api_url)
    assert response.status_code == 200, f"Status code {response.status_code} inesperado"

# Teste 2: Testar resposta de erro para moeda inexistente
def test_coin_gecko_invalid_coin():
    response = requests.get("https://api.coingecko.com/api/v3/coins/invalidcoin")
    assert response.status_code == 404, "A moeda inexistente deve retornar 404"

# Teste 3: Verificar se os dados da criptomoeda estão corretos
def test_coin_gecko_data(coin_gecko_api_url):
    response = requests.get(coin_gecko_api_url)
    data = response.json()
    assert 'id' in data and data['id'] == 'bitcoin', "ID da moeda está incorreto"
    assert 'symbol' in data and data['symbol'] == 'btc', "Símbolo da moeda está incorreto"
    assert 'name' in data and data['name'] == 'Bitcoin', "Nome da moeda está incorreto"

# Teste 4: Verificar a estrutura de dados da resposta
def test_coin_gecko_data_structure(coin_gecko_api_url):
    response = requests.get(coin_gecko_api_url)
    data = response.json()
    assert 'market_data' in data, "Chave 'market_data' não encontrada na resposta"

# Teste 5: Validar histórico de preços
def test_coin_gecko_price_history():
    response = requests.get("https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=1")
    data = response.json()
    assert 'prices' in data, "Histórico de preços não encontrado"
    assert len(data['prices']) > 0, "O histórico de preços está vazio"
