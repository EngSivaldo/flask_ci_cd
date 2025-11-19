# Este arquivo contém as correções necessárias para passar no CI/CD 
# após a mudança para renderização de templates HTML (de JSON para HTML).

import pytest
# IMPORT CORRIGIDO: Assume que 'create_app' está no arquivo 'run.py'
from run import create_app 

# --- Fixture para Configuração do Cliente de Teste ---
@pytest.fixture
def client():
    # 1. Cria a instância do aplicativo Flask
    app = create_app() 
    # 2. Configura o app para modo de teste
    app.config['TESTING'] = True
    # 3. Cria e retorna o cliente de teste
    with app.test_client() as client:
        yield client

# --- Testes Corrigidos ---

def test_index_route_returns_html(client):
    """Testa se a rota principal ('/') retorna HTML e o conteúdo esperado."""
    
    response = client.get('/')
    
    # 1. Verifica se o status HTTP é 200 (OK)
    assert response.status_code == 200
    
    # 2. Verifica se o tipo de conteúdo é HTML (Não JSON)
    assert 'text/html' in response.content_type
    
    # 3. Verifica se o conteúdo do novo index.html está presente.
    # Usamos o prefixo 'b' para indicar que estamos verificando bytes.
    # Os caracteres especiais (como 'á', 'ã') são codificados (ex: \xc3\xa1)
    assert b'P\xc3\xa1gina Inicial Show!' in response.data 
    assert b'Bem-vindo ao Meu App Flask Implementado!' in response.data

def test_about_route_returns_html(client):
    """Testa se a nova rota '/about' funciona corretamente e retorna seu HTML."""
    
    response = client.get('/about')
    
    # 1. Verifica se o status HTTP é 200 (OK)
    assert response.status_code == 200
    
    # 2. Verifica se o tipo de conteúdo é HTML
    assert 'text/html' in response.content_type
    
    # 3. Verifica se o conteúdo do about.html está presente.
    assert b'P\xc3\xa1gina Sobre' in response.data 
    assert b'Esta aplica\xc3\xa7\xc3\xa3o Flask foi implementada com sucesso' in response.data