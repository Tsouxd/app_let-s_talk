from app import create_app
import os

app = create_app()

if __name__ == "__main__":
    # Démarre l'application en mode debug sur le port 5000
    app.run(
        host=os.getenv("HOST", "127.0.0.1"),
        port=int(os.getenv("PORT", 5000)),
        debug=True
    )