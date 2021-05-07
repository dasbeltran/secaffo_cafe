import os

from flask import Flask, render_template, url_for
def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY = 'mikey',
        DATABASE_HOST = os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD = os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE_USER = os.environ.get('FLASK_DATABASE_USER'),
        DATABASE = os.environ.get('FLASK_DATABASE'),
    )
    from . import db
    db.init_app(app)

    from . import protocolo

    app.register_blueprint(protocolo.bp)
    
    @app.route('/',methods=["GET"])
    def home():
        return render_template('home.html')

    @app.route('/intermitente',methods=["GET"])
    def intermitente():
        return render_template('intermitente.html')
    
    return app