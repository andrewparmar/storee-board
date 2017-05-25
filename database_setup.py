from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Time, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

# import os
# import sys

Base = declarative_base()

class Video(Base):
	__tablename__ = 'video'

	id = Column(Integer, primary_key=True)
	video_type = Column(String(32), nullable=False)
	title = Column(String(250))
	description = Column(String(300))
	duration = Column(String(30))
	__mapper_args__ = {'polymorphic_on': video_type}


class Movie(Video):
    __tablename__ = 'movie'

    id = Column(Integer, ForeignKey('video.id'), primary_key=True)
    __mapper_args__ = {'polymorphic_identity':'movie'}
    year = Column(Integer)
    poster_mov = Column(String(250))
    youtube_trailer = Column(Text)


class TvShow(Video):
    __tablename__ = 'tv_show'

    id = Column(Integer, ForeignKey('video.id'), primary_key=True)
    __mapper_args__ = {'polymorphic_identity':'tv_show'}
    season = Column(String(100))
    episode = Column(String(100))
    poster_tv = Column(String(250))


engine = create_engine('sqlite:///video_database.db', echo=True)

Base.metadata.create_all(engine)
