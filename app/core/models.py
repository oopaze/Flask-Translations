from datetime import datetime

from app.src.db import db


class BaseModel:
    DATE_FIELDS = []

    criado_em = db.Column(db.DateTime, default=datetime.now)
    atualizado_em = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
