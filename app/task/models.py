import enum

from .src.db import db


class Tipo(enum.Enum):
    not_important = "Not Important"
    medium = "Medium"
    important = "Important"


class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    descricao = db.Column(db.Text)
    tipo = db.Column(db.Enum(Tipo))

    def __init__(self, title, descricao, tipo):
        self.title = title
        self.descricao = descricao
        self.tipo = tipo

    def __repr__(self):
        return f"Task(title={self.title}, descricao={self.descricao}, tipo={self.tipo})"

    def __str__(self):
        return f"{self.title} ({self.tipo.value})"
