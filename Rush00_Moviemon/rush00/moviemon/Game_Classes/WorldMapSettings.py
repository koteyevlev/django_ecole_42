from moviemon.Game_Classes.setting_films import list_of_films
from moviemon.Game_Classes.Moviemon import Moviemon
import json
import os

class WorldMapSettings():
    def __init__(self, rows=list(range(10)), columns=list(range(10)), player_col=0, player_row=0,
                 movieballs=0, strength=None, message=""):
        self.rows = min(10, len(rows))
        self.columns = min(10, len(columns))
        self.player_col = min(player_col, self.rows)
        self.player_row = min(player_row, self.columns)
        self.moviemon_list = generate_movies()
        self.movieballs = movieballs
        self.strength = 7
        if os.path.isfile('moviedex.json'):
            with open('moviedex.json', "r") as f:
                moviemon_list = list(dict(json.load(f)).values())
            self.strength = max(1, len(moviemon_list)) + 7



def generate_movies():
    output = dict()
    for movie_id in list_of_films:
        output[movie_id] = Moviemon(movie_id).__dict__

    with open("moviemon_info.json", "w") as outfile:
        json.dump(output, outfile)
    return output

