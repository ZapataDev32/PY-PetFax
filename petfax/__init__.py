from flask import Flask

from flask_migrate import Migrate

import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("MY_KEY")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)
    

    @app.route('/')
    def index():
        return 'Hello, PetFax!'
    
    # register pet blueprint
    from . import pet
    app.register_blueprint(pet.bp)

    # register pet blueprint
    from . import fact
    app.register_blueprint(fact.bp)

    return app