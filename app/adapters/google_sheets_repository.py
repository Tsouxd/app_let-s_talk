import json
import gspread
from google.oauth2.service_account import Credentials
from typing import List
from app.domain.models import Post
from app.adapters.repository_interface import PostRepository

class GoogleSheetsRepository(PostRepository):
    """
    Implémentation concrète du stockage utilisant l'API Google Sheets.
    Accède aux identifiants via une chaîne de caractères JSON.
    """
    def __init__(self, credentials_json_str: str, spreadsheet_id: str):
        scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]
        
        try:
            # 1. Analyse de la chaîne JSON pour la transformer en dictionnaire Python
            info = json.loads(credentials_json_str)
            
            # 2. Authentification à partir du dictionnaire (info) au lieu du fichier
            creds = Credentials.from_service_account_info(info, scopes=scopes)
            self.client = gspread.authorize(creds)
            
            # 3. Connexion à la feuille
            self.spreadsheet = self.client.open_by_key(spreadsheet_id)
            self.sheet = self.spreadsheet.get_worksheet(0)
        except Exception as e:
            raise RuntimeError(f"Erreur de connexion à Google Sheets : {str(e)}")

    def save(self, post: Post) -> None:
        try:
            row_data = post.to_row()
            self.sheet.append_row(row_data)
        except Exception as e:
            raise RuntimeError(f"Impossible d'enregistrer le message dans Google Sheets : {str(e)}")

    def get_all(self) -> List[Post]:
        try:
            records = self.sheet.get_all_records()
            posts = []
            
            for record in records:
                post_type = record.get("Type", "").strip()
                content = record.get("Contenu", "").strip()
                author = record.get("Auteur", "").strip()
                created_at = record.get("Date", "").strip()
                
                if post_type and content:
                    is_anonymous = (author == "Anonyme")
                    
                    posts.append(Post(
                        post_type=post_type,
                        content=content,
                        author=author,
                        is_anonymous=is_anonymous,
                        created_at=created_at
                    ))
            
            return list(reversed(posts))
            
        except Exception as e:
            raise RuntimeError(f"Impossible de récupérer les données depuis Google Sheets : {str(e)}")