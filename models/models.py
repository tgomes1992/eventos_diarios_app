from app import db
from datetime import datetime



class Eventos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ativo = db.Column(db.String(20), nullable=False)
    emissor = db.Column(db.String(20))
    data_base = db.Column(db.DateTime, default=datetime.utcnow)
    data_liquidacao = db.Column(db.DateTime, default=datetime.utcnow)




