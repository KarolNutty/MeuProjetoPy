import pytest
from api.api import app  # Importa a instância do Flask


@pytest.fixture
def client():
    # Configura o teste para usar o cliente do Flask
    with app.test_client() as client:
        yield client


def test_get_operadoras(client):
    # Testa a rota GET para "/api/operadoras"
    response = client.get('/api/operadoras')
    assert response.status_code == 200  # Espera o status 200 OK
    assert isinstance(response.json, list)  # Espera que a resposta seja uma lista


def test_post_operadora(client):
    # Testa a rota POST para "/api/operadoras"
    operadora_data = {
        'nome': 'Operadora Teste',
        'cnpj': '12345678000195',
        'endereco': 'Rua Teste, 123',
        'telefone': '(11) 1234-5678'
    }

    response = client.post('/api/operadoras', json=operadora_data)

    assert response.status_code == 201  # Espera o status 201 (Criado)
    assert 'id' in response.json  # Espera que o id tenha sido retornado
    assert response.json['nome'] == operadora_data['nome']  # Verifica se o nome está correto


def test_post_operadora_missing_fields(client):
    # Testa a rota POST para "/api/operadoras" com campos faltando
    operadora_data = {
        'nome': 'Operadora Teste',
        'cnpj': '12345678000195',
        'endereco': 'Rua Teste, 123'
    }

    response = client.post('/api/operadoras', json=operadora_data)

    assert response.status_code == 400  # Espera o status 400 (Bad Request)
    assert 'missing_fields' in response.json  # Espera que o erro mencione campos faltando


def test_post_operadora_invalid_json(client):
    # Testa a rota POST para "/api/operadoras" com um JSON inválido
    response = client.post('/api/operadoras', data="invalid_json")
    assert response.status_code == 400  # Espera o status 400 (Bad Request)
    assert response.json['message'] == "Requisição deve ser JSON"  # Verifica a mensagem de erro
