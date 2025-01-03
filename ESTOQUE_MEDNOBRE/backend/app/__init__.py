from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inicializa o SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configurações do aplicativo
    app.config.from_object('config')
    
    # Inicializa o banco de dados
    db.init_app(app)
    
    # Importa e registra as rotas
    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)
    
    return app
