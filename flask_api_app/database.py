from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseMixin(object):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column('created_at', db.DateTime, nullable=False,
                           default=datetime.now)
    updated_at = db.Column('updated_at', db.DateTime, nullable=False,
                           default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return '<{self.__class__.__name__}:{self.id}>'.format(self=self)
