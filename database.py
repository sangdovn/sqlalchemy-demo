from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from configs import settings

engine = create_engine(settings.database_url)

SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


Base.metadata.create_all(bind=engine)


def get_db():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
