from flask_babel import _
import enum

from app.src.db import db
from app.core.models import BaseModel


class Tipo(enum.Enum):
    pouco_importante = _("A bit important")
    importante = _("Important")
    muito_importante = _("Too much important")


class Estado(enum.Enum):
    criado = _('Created')
    iniciado = _('Started')
    pausado = _('Paused')
    finalizado = _('Finished')


class Task(BaseModel, db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    descricao = db.Column(db.Text)
    tipo = db.Column(db.Enum(Tipo), default='pouco_importante')

    estado = db.Column(db.Enum(Estado), default='criado')

    def __init__(self, title, descricao, tipo):
        self.title = title
        self.descricao = descricao
        self.tipo = tipo

    def __repr__(self):
        return f"Task(title={self.title}, descricao={self.descricao}, tipo={self.tipo})"

    def __str__(self):
        return f"{self.title} ({self.tipo.value})"
