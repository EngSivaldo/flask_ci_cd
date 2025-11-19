# Este arquivo DEVE ser o ÚNICO na pasta 'tests/'.
# Ele usa importação relativa para encontrar a função create_app() no pacote 'app/'.

import pytest

# IMPORTAÇÃO RELATIVA: Esta forma é mais robusta em ambientes de CI/CD.
# O Python tenta importar o módulo 'app' do diretório imediatamente acima da pasta 'tests'.
# Garante que ele procure a função create_app dentro de app/__init__.py
from ..app import create_app

# --- Fixture para Configuração do Cliente de Teste ---
@pytest.fixture
def client():
    """Configura o cliente de teste Flask para simular requisições."""
    # 1. Cria a instância do aplicativo Flask
    app = create_app() 
    # 2. Configura o app para modo de teste
    app.config['TESTING'] = True
    # 3. Cria e retorna o cliente de teste
    with app.test_client() as client:
        yield client

# --- Testes Corrigidos para HTML ---

def test_index_route_returns_html(client):
    """Testa se a rota principal ('/') retorna HTML e o conteúdo esperado do template."""
    
    response = client.get('/')
    
    # 1. Verifica se o status HTTP é 200 (OK)
    assert response.status_code == 200
    
    # 2. Verifica se o tipo de conteúdo é HTML (text/html)
    assert 'text/html' in response.content_type
    
    # 3. Verifica se o conteúdo do novo index.html está presente.
    # Verifica o título e uma string importante do corpo.
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