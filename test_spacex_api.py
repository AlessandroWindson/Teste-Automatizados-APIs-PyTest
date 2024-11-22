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