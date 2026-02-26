from sqlalchemy import Column,Integer,String,Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class AnalysisResult(Base):

    __tablename__="analysis"

    id=Column(Integer,primary_key=True)
    filename=Column(String)
    query=Column(String)
    result=Column(Text)