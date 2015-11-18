import flask
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    """
    A "application factory" function. It's meant to create applications
    on the fly, so that we can support multiple clients in the same app server.

    See the following URLs for more information:
    http://flask.pocoo.org/docs/patterns/appdispatch/
    http://flask.pocoo.org/docs/patterns/appfactories/

    :return: The Flask application
    :rtype: flask app
    """

    app = flask.Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

    db.init_app(app)

    @app.route('/update', methods=['POST'])
    def update():
        """

        """

        # XXX: I expect to have an Account model here, because
        # i created it during the test setup
        # import pudb; pudb.set_trace()

        return "UPDATE SUCCESS"

    return app

class Account(db.Model):
    """
    An example model, here - an Account with a username.
    """

    __tablename__ = 'account'

    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)

    def __repr__(self):
        return "<Account({}) - {}>".format(self.id, self.username)
