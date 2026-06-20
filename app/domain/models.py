from datetime import datetime
from typing import Optional

class Post:
    """
    Représente l'entité de base pour une Prière ou un Témoignage.
    """
    def __init__(
        self, 
        post_type: str,          # "priere" ou "temoignage"
        content: str, 
        author: Optional[str] = None, 
        is_anonymous: bool = True,
        created_at: Optional[str] = None
    ):
        # Validation basique du type de message
        if post_type not in ["priere", "temoignage"]:
            raise ValueError("Le type de publication doit être 'priere' ou 'temoignage'.")
            
        if not content or not content.strip():
            raise ValueError("Le contenu de la publication ne peut pas être vide.")

        self.post_type = post_type
        self.content = content.strip()
        self.is_anonymous = is_anonymous
        
        # Si anonyme ou sans auteur spécifié, on applique "Anonyme"
        self.author = "Anonyme" if is_anonymous or not author or not author.strip() else author.strip()
        
        # Date de création
        self.created_at = created_at or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_row(self) -> list:
        """
        Convertit l'objet Post en liste ordonnée pour l'insertion
        dans les lignes de Google Sheets.
        """
        return [self.created_at, self.post_type, self.author, self.content]