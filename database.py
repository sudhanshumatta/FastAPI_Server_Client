from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase,sessionmaker

from pathlib import Path

BASE_DIR=Path(__file__).resolve().parent
DB_PATH=BASE_DIR/"mydb.db"

engine=create_engine(f"sqlite:///{DB_PATH}")

class Base(DeclarativeBase):
    pass

session=sessionmaker(bind=engine)

def get_db():
    db=session()
    try:
        yield  db
    finally:
        db.close()
