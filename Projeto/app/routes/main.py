from flask import Blueprint, jsonify

main_bp = Blueprint('main_bp', __name__)

# Funções de Login
@main_bp.route('/login', methods=['POST'])
def login():
    return jsonify({'mensagem':'Realizar o login'})

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

# Função de apresentação
@main_bp.route('/')
def index():
    return jsonify({'mensagem':'Seja bem vindo(a) ao StyleSync!'})



