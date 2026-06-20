from abc import ABC, abstractmethod
from typing import List
from app.domain.models import Post

class PostRepository(ABC):
    """
    Interface définissant les opérations autorisées sur le stockage des messages.
    """
    
    @abstractmethod
    def save(self, post: Post) -> None:
        """
        Enregistre un nouveau message (Prière ou Témoignage).
        """
        pass

    @abstractmethod
    def get_all(self) -> List[Post]:
        """
        Récupère l'ensemble des messages stockés.
        """
        pass