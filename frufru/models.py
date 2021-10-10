from typing import Dict, Any, List

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Car(Base):
    __tablename__ = "cars"

    id = sa.Column(sa.Integer, primary_key=True)
    make = sa.Column(sa.String(128))
    model = sa.Column(sa.String(128), unique=True)

    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    @property
    def as_dict(self) -> Dict[str, Any]:
        return {"id": self.id, "make": self.make, "model": self.model}

    def save(self, session):
        with session.begin():
            session.add(self)

    @classmethod
    def get_list(cls, session) -> List["Car"]:
        models = []

        with session.begin():
            query = session.query(cls)
            models = query.all()

        return models


class Rate(Base):
    __tablename__ = "rates"

    id = sa.Column(sa.Integer, primary_key=True)
    mark = sa.Column(sa.Integer)  # , min=1, max=5)
    car_id = relationship("Car", order_by="Car.id")

    def __init__(self, mark: int, car_id: int):
        self.mark = mark
        self.car_id = car_id

    @property
    def as_dict(self) -> Dict[str, Any]:
        return {"id": self.id, "mark": self.mark, "car_id": self.car_id}

    def save(self, session):
        with session.begin():
            session.add(self)

    @classmethod
    def get_list(cls, session) -> List["Rate"]:
        models = []

        with session.begin():
            query = session.query(cls)
            models = query.all()

        return models
