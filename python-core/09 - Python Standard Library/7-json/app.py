import json
from pathlib import Path

# movies = [
#     { "id": 1, "title": "Terminator", "year": 1989 },
#     { "id": 2, "title": "Kindergarten Cop", "year": 1993 }
# ]

# data = json.dumps(movies) # data is json file now
# Path("movies.json").write_text(data)

data = Path("movies.json").read_text()
movies = json.loads(data) # json is loaded to movies now
print(movies)
print(movies[0]["title"])
