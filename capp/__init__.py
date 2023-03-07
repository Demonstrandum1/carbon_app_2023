from flask import Flask

application = Flask(__name__)

application.config['SECRET_KEY'] = '7bfd2e9c432da6e54b071b7828d97a22a02012d451e082a8'

from capp.home.routes import home
from capp.methodology.routes import methodology
from capp.carbon_app.routes import carbon_app
from capp.users.routes import users

application.register_blueprint(home)
application.register_blueprint(methodology)
application.register_blueprint(carbon_app)
application.register_blueprint(users)

