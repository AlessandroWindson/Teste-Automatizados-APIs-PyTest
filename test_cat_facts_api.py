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