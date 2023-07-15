from flask import Flask

def createApp():
    app = Flask(__name__)

    # secret key is a required part of flask
    # it allows us to use cookies (sessions) which are secured by
    # 64-bit encryption using the secret key found here.
    app.config['SECRET_KEY'] = 'thequickbrownfoxjumpsoverthelazydog'

    # grab endpoints
    from .views import views

    #register endpoints
    app.register_blueprint(views, url_prefix='/')

    return app