from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature
from . import db

class User(db.Model):
    """Describe columns is db"""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), nullable=False, unique=True, index=True)
    counter = db.Column(db.Integer)

    def __init__(self, email):
        self.email = email
        self.counter = 0

    def __repr__(self):
        return f'User with email {self.email} visited by Magic Link {self.counter} times'

    def generate_token(self, expiration=3600):
        """ This method generate token with default  expiration time with 1 hour"""

        s = Serializer(current_app.config['SECRET_KEY'], expiration)

        return s.dumps({'id': self.id})

    def decode_token(self, token):
        """Decoding token"""

        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except BadSignature:
            return False
        if data.get('id') != self.id:
            return False
        self.increment_counter(self.id)

    @staticmethod
    def increment_counter(user_id):
        """ Incrementing user visiting counter"""

        user = User.query.get(user_id)
        user.counter += 1
        db.session.commit()
        #Повесить ексепшен
