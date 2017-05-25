# !/usr/bin/env python

from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Video, Movie, TvShow, Base

from sqlalchemy.orm import with_polymorphic

app = Flask(__name__)


# Create session and connect to DB
engine = create_engine('sqlite:///video_database.db', echo=True)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Application Route functions
@app.route('/')
def hello_world():
    '''
    Return an html template of list of movies from database
    '''
    # videos = session.query(Video).all()
    # videos = session.query(Video).join(Movie.id)
    # videos = session.query(Movie).all() 
    # videos = session.query(TvShow).order_by(TvShow.id)
    # videos = session.query(TvShow).all()
    # for v in videos:
    # 	print v.title

    all_videos = with_polymorphic(Video, [Movie, TvShow])
    videos = session.query(all_videos).all()

    return render_template('movies.html', videos=videos)


def newVideo():

    # This needs to be a Post request handler to add new movies.
    # Do you need helper functions?
    return 0


def delVideo():

    # This needs to be a Post request handler to add new movies.
    # Do you need helper functions?
    return 0


if __name__ == '__main__':
    # app.secret_key = 'xvmZcviLG0U8z77LxgKHmgAO'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)


# TODO

# make movies.html replicat the view from movie trailer proj

# session.query(MenuItem).join(MenuItem.restaurant).filter(
#             Restaurant.id == restaurant_id).order_by(MenuItem.course)