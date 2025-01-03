import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Caminho para o banco SQLite
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'database', 'estoque.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
