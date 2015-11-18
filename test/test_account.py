
import pytest

from example import db, Account
# from example.model.account import Account

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

        path  = '/update'
        data  = { 'a' : 1 }
        ctype = 'application/json'

        resp = self.client.post(path, data=data, content_type=ctype)

        assert resp.status_code == 200
