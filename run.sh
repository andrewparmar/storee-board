#!/bin/bash

rm video_database.db
python database_setup.py
python populate_db.py

python storee-board.py