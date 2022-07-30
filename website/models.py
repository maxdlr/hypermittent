from.import db 
from flask_login import UserMixin

class Intermittence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dateDebut = db.Column(db.DateTime(timezone=True))
    dateFin = db.Column(db.DateTime(timezone=True))
    heures = db.Column(db.Integer)
    salaireBrut = db.Column(db.Integer)
    datePaiement = db.Column(db.DateTime(timezone=True))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    intermittenceData = db.relationship('Intermittence')