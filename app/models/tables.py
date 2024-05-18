from app import db
from datetime import datetime

class Brinquedo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    disponivel = db.Column(db.Boolean, default=True, nullable=False)
    categoria = db.Column(db.String(80), nullable=False)
    emprestimos = db.relationship('Emprestimo', backref='brinquedo', lazy=True)
    ultima_alteracao = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f'<Brinquedo {self.nome}>'

class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    emprestimos = db.relationship('Emprestimo', backref='professor', lazy=True)

    def __repr__(self):
        return f'<Professor {self.nome}>'

class Emprestimo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brinquedo_id = db.Column(db.Integer, db.ForeignKey('brinquedo.id'), nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'), nullable=False)
    data_emprestimo = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f'<Emprestimo {self.id}>'
