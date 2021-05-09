from moviemon.Game_Classes.WorldMapSettings import WorldMapSettings
from random import sample
import json
from moviemon.Game_Classes.setting_films import list_of_films
from moviemon.Game_Classes.Moviemon import Moviemon


class GameDataHandler():
    def __init__(self, params={"catching": False, "message": "", "last_moviemon": "", "catched_moviemon": 0}):
        self.catching = params["catching"]
        self.last_moviemon = params["last_moviemon"]
        self.message = params["message"]
        self.catched_moviemon = params["catched_moviemon"]
        self.all_moviemon = len(list_of_films)
        params.pop("catching", None)
        params.pop("all_moviemon", None)
        params.pop("message", None)
        params.pop("last_moviemon", None)
        params.pop("catched_moviemon", None)
        self.worldmap = WorldMapSettings(**params)
        self.load_movies()

    def load(self, slot=0):
        # тут загружается игра
        if slot == 0:
            output = self.dump()
        with open("game_state.json", "r") as infile:
            info = dict(json.load(infile))
            with open('moviemon_info.json') as mm:
                mmons = dict(json.load(mm))
            movie_id = None
            for id_ in mmons:
                if info['last_moviemon'] == mmons[id_]['name']:
                    movie_id = id_
        info['movie_id'] = movie_id
        return info

    """
    def load(self, slot=0):
        # тут загружается игра
        if slot == 0:
            output = self.dump()
        with open("game_state.json", "r") as infile:
            return dict(json.load(infile))
            """

    def dump(self):
        setting = dict()
        setting["rows"] = list(range(self.worldmap.rows))
        setting["columns"] = list(range(self.worldmap.columns))
        setting["player_col"] = self.worldmap.player_col
        setting["player_row"] = self.worldmap.player_row
        setting["movieballs"] = self.worldmap.movieballs
        setting["message"] = self.message
        setting["strength"] = self.get_strength()
        setting["catching"] = self.catching
        setting["last_moviemon"] = self.last_moviemon
        setting["catched_moviemon"] = self.catched_moviemon
        setting["all_moviemon"] = self.all_moviemon
        with open("game_state.json", "w") as outfile:
            json.dump(setting, outfile)
        return setting

    def generate_event(self):
        event = sample(["moviemon", "movieball"], 1)[0]
        if event == "moviemon":
            moviemon = self.get_random_movie()
            self.last_moviemon = moviemon["name"]
            self.catching = True
            self.message = "Found Moviemon - " + moviemon["name"] + ". Catch them!"
        else:
            self.catching = False
            self.worldmap.movieballs += 1
            self.message = "Your get new movieball!"


    def get_random_movie(self):
        return sample(list(self.worldmap.moviemon_list.values()), 1)[0]

    def load_default_settings(self):
        self.worldmap = WorldMapSettings()
        return self

    def get_strength(self):
        return self.worldmap.strength

    def get_movie(self, id):
        return self.worldmap.moviemon_list[id]

    def load_movies(self):
        for movie in list_of_films:
            if movie == "Mortal Combat":
                # Mock example
                self.worldmap.moviemon_list.append(Moviemon())
            else:
                # Go to imdb
                pass

    def up(self):
        self.worldmap.player_row = max(0, self.worldmap.player_row - 1)


    def down(self):
        self.worldmap.player_row = min(self.worldmap.rows - 1, self.worldmap.player_row + 1)


    def left(self):
        self.worldmap.player_col = max(0, self.worldmap.player_col - 1)


    def right(self):
        self.worldmap.player_col = min(self.worldmap.columns - 1, self.worldmap.player_col + 1)
