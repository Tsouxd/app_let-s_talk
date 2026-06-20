from app.domain.models import Post
from app.adapters.repository_interface import PostRepository

class CreatePostUseCase:
    """
    Cas d'utilisation pour créer et enregistrer une prière ou un témoignage.
    """
    def __init__(self, repository: PostRepository):
        # On injecte l'interface du repository (Inversion de dépendance)
        self.repository = repository

    def execute(self, post_type: str, content: str, author: str, is_anonymous: bool) -> None:
        # Création de l'entité du domaine (validation interne)
        post = Post(
            post_type=post_type, 
            content=content, 
            author=author, 
            is_anonymous=is_anonymous
        )
        # Sauvegarde via le repository injecté
        self.repository.save(post)