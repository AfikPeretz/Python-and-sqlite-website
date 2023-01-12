from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager



db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from website.models import User, Note #we does this even if we not going to use it just becouse we want to make sure
    #that the program load this file before we initialize or create out db
    create_database(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app
    
    
def create_database(app):
    if not os.path.exists('websitw/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database')
