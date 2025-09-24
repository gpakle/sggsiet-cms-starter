import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin
from flask_wtf.csrf import CSRFProtect
from .config import DevConfig, ProdConfig

db = SQLAlchemy()
login = LoginManager()
csrf = CSRFProtect()
admin = Admin(name="SGGSIET CMS", template_mode='bootstrap4')

def create_app(config_object=None):
    app = Flask(__name__, static_folder='static', template_folder='templates')
    # Load config from env or provided object
    if config_object:
        app.config.from_object(config_object)
    else:
        env = os.getenv('FLASK_ENV', 'production')
        if env == 'development':
            app.config.from_object(DevConfig)
        else:
            app.config.from_object(ProdConfig)

    # Override from .env
    from dotenv import load_dotenv
    load_dotenv()

    db.init_app(app)
    login.init_app(app)
    csrf.init_app(app)
    admin.init_app(app)

    # blueprints
    from .auth import auth_bp
    from .cms import cms_bp
    from .admin.views import init_admin
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(cms_bp)
    init_admin(admin, app)

    # create instance media dir
    os.makedirs(app.config.get('MEDIA_FOLDER', os.path.join(app.instance_path, 'media')), exist_ok=True)

    return app
