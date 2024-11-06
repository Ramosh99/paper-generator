from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    doc_type = Column(String)  # past_paper or theory_note
    year = Column(Integer, nullable=True)
    content_hash = Column(String, unique=True)
    upload_date = Column(DateTime)

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    document_id = Column(Integer, ForeignKey("documents.id"))
    topic = Column(String)
    difficulty = Column(Integer)
    year = Column(Integer, nullable=True)