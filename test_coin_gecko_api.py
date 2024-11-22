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
import responses

# URL base da API CoinGecko
BASE_URL = "https://api.coingecko.com/api/v3/coins/bitcoin"

# Teste 1: Verificar se a API retorna o status correto (200) com mock
@responses.activate
def test_coin_gecko_success():
    """
    Testa se a resposta da API retorna o status 200
    para a URL da moeda Bitcoin.
    """
    # Mock da resposta
    responses.add(responses.GET, BASE_URL, json={'id': 'bitcoin', 'symbol': 'btc', 'name': 'Bitcoin'}, status=200)

    response = requests.get(BASE_URL)
    assert response.status_code == 200, f"Status code {response.status_code} inesperado"
    data = response.json()
    assert 'id' in data and data['id'] == 'bitcoin', "ID da moeda está incorreto"
    assert 'symbol' in data and data['symbol'] == 'btc', "Símbolo da moeda está incorreto"
    assert 'name' in data and data['name'] == 'Bitcoin', "Nome da moeda está incorreto"

# Teste 2: Testar resposta de erro para moeda inexistente com mock
@responses.activate
def test_coin_gecko_invalid_coin():
    """
    Testa a resposta da API para uma moeda inexistente.
    Espera-se que retorne o status 404.
    """
    # Mock de uma resposta 404 para moeda inexistente
    responses.add(responses.GET, "https://api.coingecko.com/api/v3/coins/invalidcoin", status=404)

    response = requests.get("https://api.coingecko.com/api/v3/coins/invalidcoin")
    assert response.status_code == 404, "A moeda inexistente deve retornar 404"

# Teste 3: Verificar se os dados da criptomoeda estão corretos com mock
@responses.activate
def test_coin_gecko_data():
    """
    Testa se os dados retornados pela API para a moeda Bitcoin
    contêm os valores esperados de 'id', 'symbol' e 'name'.
    """
    # Mock da resposta
    responses.add(responses.GET, BASE_URL, json={'id': 'bitcoin', 'symbol': 'btc', 'name': 'Bitcoin'}, status=200)

    response = requests.get(BASE_URL)
    data = response.json()

    # Verificar se a chave 'id' existe e seu valor é 'bitcoin'
    assert 'id' in data and data['id'] == 'bitcoin', "ID da moeda está incorreto"
    
    # Verificar se a chave 'symbol' existe e seu valor é 'btc'
    assert 'symbol' in data and data['symbol'] == 'btc', "Símbolo da moeda está incorreto"
    
    # Verificar se a chave 'name' existe e seu valor é 'Bitcoin'
    assert 'name' in data and data['name'] == 'Bitcoin', "Nome da moeda está incorreto"

# Teste 4: Verificar a estrutura de dados da resposta com mock
@responses.activate
def test_coin_gecko_data_structure():
    """
    Testa se a resposta da API contém a chave 'market_data',
    que é essencial para obter dados de mercado da criptomoeda.
    """
    # Mock da resposta
    responses.add(responses.GET, BASE_URL, json={'market_data': {'current_price': {'usd': 40000}}}, status=200)

    response = requests.get(BASE_URL)
    data = response.json()

    # Verificar se a chave 'market_data' existe na resposta
    assert 'market_data' in data, "Chave 'market_data' não encontrada na resposta"

# Teste 5: Validar histórico de preços com mock
@responses.activate
def test_coin_gecko_price_history():
    """
    Testa a resposta da API para o histórico de preços da moeda Bitcoin
    nos últimos 1 dia (em USD).
    Espera-se que a chave 'prices' esteja presente e que contenha dados.
    """
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=1"
    
    # Mock da resposta com dados fictícios de preços
    responses.add(responses.GET, url, json={'prices': [[1623772800000, 40000], [1623859200000, 41000]]}, status=200)

    response = requests.get(url)
    data = response.json()

    # Verificar se a chave 'prices' existe na resposta
    assert 'prices' in data, "Histórico de preços não encontrado"
    
    # Verificar se o histórico de preços contém dados
    assert len(data['prices']) > 0, "O histórico de preços está vazio"