from app import create_app, db
from app.models import User, Tenant, Page, Media, Department, Faculty
from flask_migrate import Migrate

app = create_app()
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Tenant': Tenant,
        'Page': Page,
        'Media': Media,
        'Department': Department,
        'Faculty': Faculty,
    }

if __name__ == "__main__":
    app.run()
