import os
from unittest import TestCase
from flask import url_for, request
from app import create_app, db
from config import TestConfig
from app.models import User


class ClientTestCase(TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client(use_cookies=True)
        self.db_url = TestConfig.SQLALCHEMY_DATABASE_URI

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        os.remove('test.sqlite')

    def test_404(self):
        """This test checks the behavior for invalid url"""

        res = self.client.get('invalid/url')
        self.assertTrue(res.status_code == 404)

    def test_create_delete_email(self):
        """This test checks core/create_delete url"""

        response = self.client.post(url_for('core.create_delete_email'),
                                    data={'email': 'test@mail.com'},)
        self.assertTrue(response.status_code == 200)
        self.assertEqual(request.path, url_for('core.index'))

    def test_index(self):
        """This test checks core/index url"""

        new_user = User(email='test@mail.com')
        db.session.add(new_user)
        db.session.commit()

        response = self.client.get(url_for('core.index'))
        self.assertTrue(response.status_code == 200)
        self.assertIn(b'test@mail.com', response.data)
