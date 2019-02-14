from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    pitches = db.relationship('Pitch',backref = 'pitches',lazy = "dynamic")

    def __repr__(self):
        return f'User {self.username}'