import flask
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Account(db.Model):
    """
    An example model, here - an Account with a username.
    """

    __tablename__ = 'account'

    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)

    def __repr__(self):
        return "<Account({}) - {}>".format(self.id, self.username)

def create_app():

    app = flask.Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'

    db.init_app(app)

    @app.route('/update', methods=['POST'])
    def update():
        """

        """

        # XXX: I expect to have an Account model here, because
        # i created it during the test setup
        # import pudb; pudb.set_trace()

        print "Expect an account model"
        print Account.query.all()

        return "UPDATE SUCCESS"

    return app
