from flask import Blueprint, jsonify, request
from app.models.user import LoginPlayLoad
from pydantic import ValidationError

main_bp = Blueprint('main_bp', __name__)

# Funções de Login
@main_bp.route('/login', methods=['POST'])
def login():
    try:
        raw_data = request.get_json()
        user_data = LoginPlayLoad(**raw_data)
    except ValidationError as e:
        return jsonify({'error': e.errors()}), 400
    except Exception as e:
        jsonify({'error': 'Erro durante a requisição do dado'}), 500
    
    return jsonify({'mensagem':f'Realizar o login do usuário {user_data.model_dump_json()}'})

# Funções de Produtos
@main_bp.route('/products')
def get_products():
    return jsonify({'mensagem':'Listagem de produtos'})

@main_bp.route('/products', methods=['POST'])
def create_products():
    return jsonify({'mensagem':'Criação de produtos'})

@main_bp.route('/products/<int:product_id>')
def get_product_by_id(product_id):
    return jsonify({'mensagem':f'Apresentação do produto com id {product_id}'})

@main_bp.route('/products/<int:product_id>', methods=['PUT'])
def update_products(product_id):
    return jsonify({'mensagem':f'Atualização do produto com id {product_id}'})

@main_bp.route('/products/<int:product_id>', methods=['DELETE'])
def delete_products(product_id):
    return jsonify({'mensagem':f'Deleção do produto com id {product_id}'})

# Função de vendas
@main_bp.route('/sales/upload', methods=['POST'])
def upload_sales():
    return jsonify({'mensagem':'Upload dos arquivos de vendas'})

# Função de categoria
@main_bp.route('/category')
def get_category():
    return jsonify({'mensagem':'Listagem de categorias'})

@main_bp.route('/category', methods=['POST'])
def create_category():
    return jsonify({'mensagem':'Criação de Categoria'})

@main_bp.route('/category/<int:category_id>')
def get_category_by_id(category_id):
    return jsonify({'mensagem':f'Apresentação da categoria com id {category_id}'})

@main_bp.route('/category/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    return jsonify({'mensagem':f'Atualização da categoria com id {category_id}'})

@main_bp.route('/category/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    return jsonify({'mensagem':f'Deleção da categoria com id {category_id}'})

# Função de apresentação
@main_bp.route('/')
def index():
    return jsonify({'mensagem':'Seja bem vindo(a) ao StyleSync!'})



