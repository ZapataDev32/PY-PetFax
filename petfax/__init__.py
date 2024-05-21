from flask import Flask



def create_app():
    app = Flask(__name__)
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    @app.route('/')
    def hello():
        return 'Hello, PetFax!'
    
    # register pet blueprint
    from . import pet
    app.register_blueprint(pet.bp)
    
    # register pet blueprint
    from . import fact
    app.register_blueprint(fact.bp)

    return app