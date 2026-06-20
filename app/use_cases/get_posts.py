from typing import List, Dict
from app.adapters.repository_interface import PostRepository

class GetPostsUseCase:
    """
    Cas d'utilisation pour récupérer l'ensemble des publications,
    classées par type pour l'affichage en deux colonnes.
    """
    def __init__(self, repository: PostRepository):
        self.repository = repository

    def execute(self) -> Dict[str, List]:
        # Récupération de tous les messages depuis la source de données
        all_posts = self.repository.get_all()
        
        # Tri et répartition des messages
        sorted_posts = {
            "prieres": [post for post in all_posts if post.post_type == "priere"],
            "temoignages": [post for post in all_posts if post.post_type == "temoignage"]
        }
        
        return sorted_posts