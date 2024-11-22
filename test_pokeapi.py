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