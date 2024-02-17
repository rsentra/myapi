from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import contextlib

SQLALCHEMY_DATABASE_URL = "sqlite:///./myapi.db"  #root에 저장함

#커넥션 풀 생성
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# @contextlib.contextmanager  #=> router에서 depends를 사용하므로 불필요해짐
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()