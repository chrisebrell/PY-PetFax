from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "This is my home page!"

    from . import pets
    app.register_blueprint(pets.bp)
    
    return app