from flask import Blueprint, jsonify, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # Agora renderiza a página HTML em vez de JSON
    return render_template('index.html')

@main.route('/about')
def about():
    # Exemplo de outra rota
    return render_template('about.html')