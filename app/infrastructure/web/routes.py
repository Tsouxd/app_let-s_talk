from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.infrastructure.config import Config
from app.adapters.google_sheets_repository import GoogleSheetsRepository
from app.use_cases.create_post import CreatePostUseCase
from app.use_cases.get_posts import GetPostsUseCase

web_blueprint = Blueprint(
    'web', 
    __name__, 
    template_folder='templates',
    static_folder='static',
    static_url_path='/web_static'  # Évite le conflit d'adresse URL
)

repository = GoogleSheetsRepository(
    credentials_json_str=Config.GOOGLE_CREDENTIALS_PATH,
    spreadsheet_id=Config.SPREADSHEET_ID
)

@web_blueprint.route('/', methods=['GET'])
def index():
    """Page d'accueil : Interface divisée en 2 blocs."""
    try:
        get_posts_uc = GetPostsUseCase(repository)
        posts_by_type = get_posts_uc.execute()
    except Exception as e:
        posts_by_type = {"prieres": [], "temoignages": []}
        flash(f"Erreur lors de la récupération des données : {str(e)}", "danger")

    return render_template(
        'index.html', 
        prieres=posts_by_type["prieres"], 
        temoignages=posts_by_type["temoignages"]
    )

@web_blueprint.route('/publier/<post_type>', methods=['GET'])
def show_form(post_type):
    """Affiche le formulaire dédié selon le type choisi (priere ou temoignage)."""
    if post_type not in ['priere', 'temoignage']:
        return redirect(url_for('web.index'))
    return render_template('form.html', post_type=post_type)

@web_blueprint.route('/publier/<post_type>', methods=['POST'])
def handle_form(post_type):
    """Traite la soumission du formulaire dédié."""
    if post_type not in ['priere', 'temoignage']:
        return redirect(url_for('web.index'))

    content = request.form.get('content')
    author = request.form.get('author')
    is_anonymous = request.form.get('is_anonymous') == 'on'

    try:
        create_post_uc = CreatePostUseCase(repository)
        create_post_uc.execute(
            post_type=post_type,
            content=content,
            author=author,
            is_anonymous=is_anonymous
        )
        flash("Votre publication a été enregistrée avec succès.", "success")
    except Exception as e:
        flash(f"Une erreur est survenue lors de l'enregistrement : {str(e)}", "danger")

    return redirect(url_for('web.index'))