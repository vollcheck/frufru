import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.orm import scoping

from frufru.database import models


class Manager:
    def __init__(self, connection=None):
        self.connection = connection

        self.engine = sa.create_engine(connection)
        self.db_session = scoping.scoped_session(
            orm.sessionmaker(bind=self.engine, autocommit=True)
        )

    @property
    def session(self):
        return self.db_session()

    def setup(self):
        try:
            models.Base.metadata.create_all(self.engine)
        except Exception as e:
            # log
            print(f"Could not initialize database: {e}")
