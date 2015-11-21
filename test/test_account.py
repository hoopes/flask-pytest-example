
import pytest

from example import db, Account

@pytest.mark.usefixtures('client_class')
class TestAccounts(object):

    def test_update_view(self):
        """

        """

        test_acct = Account(username='abc')

        # add what i expect to be a model existing for the duration
        # of this test only
        db.session.add(test_acct)
        db.session.commit()

        resp = self.client.post('/update',
                                data={'a':1},
                                content_type='application/json')

        assert resp.status_code == 200
