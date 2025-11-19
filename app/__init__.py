from flask import Flask

# A função create_app deve estar aqui
def create_app():
    # 1. Cria a instância do Flask
    app = Flask(__name__)

    # 2. Configuração (se houver)
    # app.config.from_object('config.Config')

    # 3. Importa e Registra as Blueprints (rotas)
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app