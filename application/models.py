from application import db

class Players(db.Model):
    player_id       =   db.Column(db.Integer, primary_key=True)
    player_name     =   db.Column(db.String(50), nullable=False)
    player_class    =   db.Column(db.String(50), unique=False, nullable=False)
    level           =   db.Column(db.Integer, nullable=False)
    items           =   db.relationship('Items', backref='players')

class Items(db.Model):
    item_id     =   db.Column(db.Integer, primary_key=True)
    item_name   =   db.Column(db.String(50), nullable=False)
    value       =   db.Column(db.String(10), nullable=False)
    weight      =   db.Column(db.String(10), nullable=False)
    rarity      =   db.Column(db.String(50), nullable=False)
    owner       =   db.Column(db.Integer, db.ForeignKey('players.player_id'))