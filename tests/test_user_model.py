import os
from unittest import TestCase
from app import create_app, db
from app.models import User
from config import TestConfig


class UserModelTestCase(TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client(use_cookies=True)
        self.db_url = TestConfig.SQLALCHEMY_DATABASE_URI

        self.user = User(email='test@mail.com')
        db.session.add(self.user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        os.remove('test.sqlite')

    def test_generate_token(self):

        token = self.user.generate_token()
        self.assertEqual(self.user, self.user.decode_token(token))

    def test_increment_counter(self):

        counter = self.user.counter
        self.user.increment_counter()
        self.assertEqual(counter+1, self.user.counter)
