import pytest

from example import create_app, db as _db
from example import Account

@pytest.fixture(scope='session')
def app(request):
    """Session-wide test `Flask` application."""

    return create_app()

@pytest.fixture(scope='session')
def db(app, request):
    """Session-wide test database."""

    _db.drop_all()
    _db.create_all()

    return _db

@pytest.yield_fixture(scope='function', autouse=True)
def session(db, request):
    """Creates a new database session for a test."""

    conn = _db.engine.connect()
    txn = conn.begin()

    options = dict(bind=conn, binds={})
    session = _db.create_scoped_session(options=options)

    _db.session = session

    yield session

    session.remove()
    txn.rollback()
    conn.close()

    print "I expect no accounts now"
    print Account.query.all()

