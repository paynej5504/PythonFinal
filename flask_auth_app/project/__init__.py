# import statements
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy, BaseQuery
from flask_login import LoginManager
from sqlalchemy import update


# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # connection key to database
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    # connection srting goes in line 17 between the ' '
    app.config['SQLALCHEMY_DATABASE_URI'] = ''
    #fix deprication error
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)



    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

#import User from models file
    from .models import User


    @login_manager.user_loader
    # get user id
    def load_user(user_id):
        return User.query.get(int(user_id))


    db.init_app(app)




    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
