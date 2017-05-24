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

# movie1 = Movie(title="Vaastav", duration="01:01:01")

# movie2 = Movie(title="Snatch", duration="02:02:02")

movie3 = Movie(title="Ring", duration="01:01:03")

movie4 = Movie(title="Rush", duration="02:02:04")

objects = [movie3, movie4]
session.bulk_save_objects(objects)

# session.add(movie1, movie2)
session.commit()

print "added menu items!"
