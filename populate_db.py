from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Video, Movie, TvShow, Base

engine = create_engine('sqlite:///video_database.db', echo=True)
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Add titles

# movie1 = Movie(title="Vaastav"), duration="01:01:01")

# movie2 = Movie(title="Snatch"), duration="02:02:02")

# tv1 = TvShow(title="breaking bad1",
#              season="1",
#              episode="2",
#              duration="01:01:03")

# tv2 = TvShow(title="breaking bad2",
#              season="2",
#              episode="2",
#              duration="01:01:03")

# tv3 = TvShow(title="breaking bad3",
#              season="3",
#              episode="2",
#              duration="01:01:03")

# movie3 = Movie(title="Ring",
#                duration="01:01:03")

# movie4 = Movie(title="Rush",
#                duration="02:02:04",
#                year="1985",
#                poster_mov="https://tinyurl.com/nxfz9ff")


def trailer_parser(trailer_url):
    trailer_url_min = trailer_url.replace('https://www.youtube.com/watch?v=','')
    return trailer_url_min

toy_story = Movie(
    title="Toy Story", description="a story of a boys toys",
    poster_mov="https://images-na.ssl-images-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_UX182_CR0,0,182,268_AL_.jpg",
    youtube_trailer=trailer_parser("https://www.youtube.com/watch?v=KYz2wyBy3kc"), duration="81 min")

man_from_earth = Movie(
        title="Man From Earth", description="An unaging man",
        poster_mov="http://ia.media-imdb.com/images/M/MV5BNjUwMDQ2NTQxMF5BMl5BanBnXkFtZTcwMDQ4NDIzMQ@@._V1_SY317_CR15,0,214,317_AL_.jpg",  # noqa
        youtube_trailer=trailer_parser("https://www.youtube.com/watch?v=9mOIxyRTY5I"), duration="87 min")

reservoir_dogs = Movie(
    title="Reservoir Dogs", description="A jwewelery heist gone wrong",
    poster_mov="http://tinyurl.com/pxj87ly",
    youtube_trailer=trailer_parser("https://www.youtube.com/watch?v=vayksn4Y93A"), duration="99 min")

full_metal_jacekt = Movie(
        title="Full Metal Jacket", description="Effects of the Vietnam War",
        poster_mov="https://images-na.ssl-images-amazon.com/images/M/MV5BNzc2ZThkOGItZGY5YS00MDYwLTkyOTAtNDRmZWIwMGRhYTc0L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
        youtube_trailer=trailer_parser("https://www.youtube.com/watch?v=Ks_MbPPkhmA"), duration="116 min")

lord_of_war = Movie(
        title="Lord of War", description="The best arms dealer in the world",
        poster_mov="http://ia.media-imdb.com/images/M/MV5BMjEzNDM2OTgzN15BMl5BanBnXkFtZTcwMzU3MTIzMQ@@._V1_SX214_AL_.jpg",  # noqa
        youtube_trailer=trailer_parser("https://www.youtube.com/watch?v=Ej83QvHuiNI"), duration="142 min")

snatch = Movie(
        title="Snatch", description="All about a priceless stolen diamond", poster_mov="http://ia.media-imdb.com/images/M/MV5BMTk5NzE0MDQyNl5BMl5BanBnXkFtZTcwNzk4Mjk3OA@@._V1_SY317_CR2,0,214,317_AL_.jpg",  # noqa
        youtube_trailer=trailer_parser("https://www.youtube.com/watch?v=ni4tEtuTccc"), duration="102 min")

gravity = Movie(
        title="Gravity", description="The Dangers of Space",
        poster_mov="http://ia.media-imdb.com/images/M/MV5BNjE5MzYwMzYxMF5BMl5BanBnXkFtZTcwOTk4MTk0OQ@@._V1_SY317_CR0,0,214,317_AL_.jpg",  # noqa
        youtube_trailer=trailer_parser("https://www.youtube.com/watch?v=OiTiKOy59o4"), duration="102 min")

back_to_the_future = Movie(
        title="Back to the Future", description="Coolest Time Travel",
        poster_mov="http://ia.media-imdb.com/images/M/MV5BMjA5NTYzMDMyM15BMl5BanBnXkFtZTgwNjU3NDU2MTE@._V1_SX214_AL_.jpg",  # noqa
        youtube_trailer=trailer_parser("https://www.youtube.com/watch?v=qvsgGtivCgs"), duration="116 min")

oldboy = Movie(
        title="Oldboy", description="Twisted",
        poster_mov="http://ia.media-imdb.com/images/M/MV5BMTI3NTQyMzU5M15BMl5BanBnXkFtZTcwMTM2MjgyMQ@@._V1_SY317_CR0,0,214,317_AL_.jpg",  # noqa
        youtube_trailer=trailer_parser("https://www.youtube.com/watch?v=2HkjrJ6IK5E"), duration="116 min")


# Creating list of movies to be used to generate html page. #
objects = (
    toy_story, man_from_earth, reservoir_dogs, full_metal_jacekt,
    lord_of_war, snatch, gravity, back_to_the_future, oldboy)
session.bulk_save_objects(objects)


# objects = [movie3, movie4, tv1, tv2, tv3, ]
# session.bulk_save_objects(objects)

# session.add(movie1, movie2)
session.commit() 

print "added menu items!"


# TODO
# 