import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, String, Numeric, DateTime, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime, timezone

load_dotenv()
URL_BANK = os.getenv("DATABASE_URL")
if not URL_BANK:
    raise ValueError("DATABASE_URL Not found. Check the file .env")

Base = declarative_base()

class Tabel(Base):
    __tablename__ = 'History'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    Product = Column(String, nullable=False)
    Price = Column(String, nullable=False)
    Date = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

engine = create_engine(URL_BANK)
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

def get_session():
    return Session()
