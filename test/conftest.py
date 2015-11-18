import os
import pytest

from example import create_app, db as _db

@pytest.fixture(scope='session')
def app(request):
    """Session-wide test `Flask` application."""

    app = create_app()

    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)

    return app

@pytest.fixture(scope='session')
def db(app, request):
    """Session-wide test database."""

    _db.init_app(app)
    _db.drop_all()
    _db.create_all()

    return _db

@pytest.fixture(scope='function', autouse=True)
def session(db, request):
    """Creates a new database session for a test."""

    conn = _db.engine.connect()
    txn = conn.begin()

    options = dict(bind=conn, binds={})
    session = _db.create_scoped_session(options=options)

    _db.session = session

    def teardown():
        txn.rollback()
        conn.close()
        session.remove()

        # XXX: Install a debugger here! The model I added
        # in the test should be gone!!!
        # import pudb; pudb.set_trace()

    request.addfinalizer(teardown)
    return session
