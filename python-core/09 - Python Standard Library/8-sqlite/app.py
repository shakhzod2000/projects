import sqlite3
import json
from pathlib import Path

# load json file to 'movies' variable
movies = json.loads((Path(__file__).parent / ".." / "7-json" / "movies.json").read_text()) # __file__ gives abs path of curr script

movies = json.loads((Path(__file__).parent / "../7-json/movies.json").read_text()) # .parent gets dir of the script

# insert json values to 'Movies' table in 'db.sqlite3' database
# with sqlite3.connect("db.sqlite3") as conn:
#     command = "INSERT INTO Movies VALUES(?, ?, ?)"
#     for movie in movies:
#         conn.execute(command, tuple(movie.values()))
#     conn.commit() # we only need it when writing to DB


with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    # conn.execute() returns a cursor(an iterable object)
    cursor = conn.execute(command)
    # once we iterate with for loop, we go to end of cursor
    # and can't read again
    # for row in cursor:
    #     print(row)
    movies = cursor.fetchall() # returns all rows of table(list of tuples)
    print(movies)
    # conn.commit() # no need when reading from DB

