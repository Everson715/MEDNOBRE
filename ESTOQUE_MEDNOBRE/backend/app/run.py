from app import create_app

# Inicializa a aplicação Flask
app = create_app()

# Executa o servidor no modo local
if __name__ == "__main__":
    app.run(debug=True)
