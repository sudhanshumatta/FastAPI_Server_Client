from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase,sessionmaker
engine=create_engine('sqlite:///mydb.db')
class Base(DeclarativeBase):
    pass

session=sessionmaker(bind=engine)

def get_db():
    db=session()
    try:
        yield  db
    finally:
        db.close()
