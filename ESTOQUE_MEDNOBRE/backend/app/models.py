from . import db

# Tabela Fornecedor
class Fornecedor(db.Model):
    __tablename__ = 'fornecedor'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(100))
    endereco = db.Column(db.String(200))

# Tabela Item
class Item(db.Model):
    __tablename__ = 'item'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    quantidade_estoque = db.Column(db.Integer, default=0)
    data_validade = db.Column(db.Date)
    fornecedor_id = db.Column(db.Integer, db.ForeignKey('fornecedor.id'))
    
    fornecedor = db.relationship('Fornecedor', backref='itens')

# Tabela Usuario
class Usuario(db.Model):
    __tablename__ = 'usuario'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    papel = db.Column(db.String(20), nullable=False)

# Tabela Transacao
class Transacao(db.Model):
    __tablename__ = 'transacao'
    
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(10), nullable=False)  # entrada ou saída
    quantidade = db.Column(db.Integer, nullable=False)
    data = db.Column(db.DateTime, default=db.func.current_timestamp())
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    
    item = db.relationship('Item', backref='transacoes')
    usuario = db.relationship('Usuario', backref='transacoes')
