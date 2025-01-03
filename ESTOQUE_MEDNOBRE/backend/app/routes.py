from flask import Blueprint, jsonify, request
from .models import db, Fornecedor, Item, Usuario, Transacao

bp = Blueprint('routes', __name__)

# Rota para listar todos os itens
@bp.route('/itens', methods=['GET'])
def get_itens():
    itens = Item.query.all()
    return jsonify([{
        'id': item.id,
        'nome': item.nome,
        'tipo': item.tipo,
        'quantidade_estoque': item.quantidade_estoque,
        'data_validade': item.data_validade
    } for item in itens])

# Rota para adicionar um novo item
@bp.route('/itens', methods=['POST'])
def add_item():
    data = request.json
    item = Item(
        nome=data['nome'],
        tipo=data['tipo'],
        quantidade_estoque=data['quantidade_estoque'],
        data_validade=data.get('data_validade'),
        fornecedor_id=data.get('fornecedor_id')
    )
    db.session.add(item)
    db.session.commit()
    return jsonify({'message': 'Item adicionado com sucesso!'}), 201

# Rota para registrar uma transação
@bp.route('/transacoes', methods=['POST'])
def add_transacao():
    data = request.json
    transacao = Transacao(
        tipo=data['tipo'],
        quantidade=data['quantidade'],
        item_id=data['item_id'],
        usuario_id=data['usuario_id']
    )
    # Atualiza a quantidade do item no estoque
    item = Item.query.get(data['item_id'])
    if data['tipo'] == 'entrada':
        item.quantidade_estoque += data['quantidade']
    elif data['tipo'] == 'saida':
        item.quantidade_estoque -= data['quantidade']
    db.session.add(transacao)
    db.session.commit()
    return jsonify({'message': 'Transação registrada com sucesso!'}), 201
