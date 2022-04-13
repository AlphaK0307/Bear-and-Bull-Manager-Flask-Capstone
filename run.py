from app import app
from app.models import User


@app.shell_context_processor
def makae_context():
    return {'User': User}
