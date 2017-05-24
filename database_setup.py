from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Time, Text  # ForeignKey,
from sqlalchemy.ext.declarative import declarative_base

# import os
# import sys

Base = declarative_base()

# class Video(Base):
# 	__tablename__ = 'movie'

# 	id= Column(Integer, primary_key=True)
# 	title = Column(String(250))
# 	duration = Column(Time)


class Movie(Base):
    __tablename__ = 'movie'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    duration = Column(Time)
    picture = Column(String(250))


class TvShow(Base):
    __tablename__ = 'tv_show'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    season = Column(String(100))
    episode = Column(String(100))
    duration = Column(Time)


engine = create_engine('sqlite:///:memory:', echo=True)

Base.metadata.create_all(engine)
