from django.shortcuts import render, redirect
import json
import os
from random import choices

from moviemon.Game_Classes.GameDataHandler import GameDataHandler, Moviemon

def index(request):
    return render(request, "title_screen.html")


def options(request):
    return render(request, "options.html")


def load_game(request):
    slots = get_slots_info()
    return render(request, "load_game.html", dict(slots))


def load_game_action(request, action):
    slots = get_slots_info()
    if action == "down":
        if slots["picked"] < 2:
            slots["picked"] += 1
    elif action == "up":
        if slots["picked"] > 0:
            slots["picked"] -= 1
    elif action == "load":
        return load_game_from_file(slots["picked"], slots)
    with open("slots_state.json", "w") as outfile:
        json.dump(slots, outfile)
    return redirect("/options/load_game")


def save_game(request):
    slots = get_slots_info()
    return render(request, "save_game.html", dict(slots))


def save_game_action(request, action):
    slots = get_slots_info()
    if action == "down":
        if slots["picked"] < 2:
            slots["picked"] += 1
    elif action == "up":
        if slots["picked"] > 0:
            slots["picked"] -= 1
    elif action == "save":
        save_game_to_file(slots["picked"], slots)
    with open("slots_state.json", "w") as outfile:
        json.dump(slots, outfile)
    return redirect("/options/save_game")


def worldmap(request, slot=0, game=None):
    if slot != 0:
        #load game
        pass
    elif game == None:
        game = create_game()

    return render(request, "worldmap.html", game.load())


def action(request, action=None):
    game = create_game()
    print(action)
    if action:
        if action == "delete_game":
            print("remove")
            if os.path.isfile('game_state.json'):
                os.remove("game_state.json")
            if os.path.isfile('moviedex.json'):
                os.remove("moviedex.json")
            game = create_game()
        else:
            game.generate_event()
        if action == "up":
            game.up()
        elif action == "down":
            game.down()
        elif action == "left":
            game.left()
        elif action == "right":
            game.right()
    game.dump()
    return redirect("worldmap")


def battle(request, movie_id):
    with open("game_state.json", "r") as infile:
        params = dict(json.load(infile))
    if params["message"] == "Your get new movieball!":
        return redirect("worldmap")
    else:
        info = dict()
        with open("game_state.json", "r") as infile:
            params = dict(json.load(infile))
        if params["movieballs"] <= 0:
            params["message"] = "Your Movieball is over. Find them and catch again!"
            with open("game_state.json", "w") as outfile:
                json.dump(params, outfile)
            return redirect("worldmap")
        info["rating"] = get_rating(movie_id)
        info["strength"] = params["strength"]
        with open("moviemon_info.json", "r") as infile:
            moviemon = dict(json.load(infile))
        info["poster"] = moviemon[movie_id]["poster"]
        info["movieballs"] = params["movieballs"]
        info["winning_rate"] = get_winning_rate(float(info["strength"]), info["rating"])
        with open("battle_info.json", "w") as outfile:
            json.dump(info, outfile)
        return render(request, "battle.html", info)


def battle_action(request, movie_id, action):
    if action and action == "throw":
        if not os.path.isfile('battle_info.json'):
            return redirect("worldmap")
        with open("battle_info.json", "r") as infile:
            battle = dict(json.load(infile))
        with open("game_state.json", "r") as infile:
            game = dict(json.load(infile))
        sampl = [0, 1]
        probability = [1 - (int(battle["winning_rate"]) / 100), int(battle["winning_rate"]) / 100]
        #probability = [0.5, 0.5]
        answer = choices(sampl, probability)
        game["movieballs"] -= 1
        print(answer, probability)
        if answer[0] == 0:
            pass
        else:
            if not os.path.isfile('moviedex.json'):
                with open("moviedex.json", "w") as outfile:
                    json.dump({}, outfile)
            with open("moviedex.json", "r") as infile:
                moviedex = dict(json.load(infile))
            with open("moviemon_info.json", "r") as infile:
                moviemon_info = dict(json.load(infile))
            moviedex[movie_id] = moviemon_info[movie_id]
            with open("moviedex.json", "w") as outfile:
                json.dump(moviedex, outfile)
            game["message"] = "Congratulations! You caught him!"
            game["catched_moviemon"] = len(moviedex.keys())
            with open("game_state.json", "w") as outfile:
                json.dump(game, outfile)
            if os.path.isfile('battle_info.json'):
                os.remove("battle_info.json")
            return redirect("worldmap")

        with open("game_state.json", "w") as outfile:
            json.dump(game, outfile)
        return redirect("../../battle/" + movie_id)



def get_rating(movie_id):
    with open("moviemon_info.json", "r") as infile:
        params = dict(json.load(infile))
    if movie_id in params:
        return float(params[movie_id]["rating"])
    else:
        print("default monster")
        return 5


def get_winning_rate(user, moviemon):
    calculated = min(50 - (moviemon * 10) + (user * 5), 90)
    return max(1, calculated)




def detail(request, movie_id):
    return render(request, "detail.html", {'moviemon': Moviemon(movie_id)})


def moviedex(request):
    if os.path.isfile('moviedex.json'):
        with open('moviedex.json', "r") as f:
            moviemon_list = dict(json.load(f)).values()
    else:
        moviemon_list = dict()
    #with open('moviemon_info.json') as f:
    #    moviemon_list = dict(json.load(f)).values()
    return render(request, "moviedex.html", {'moviemon_list': moviemon_list})


def create_game():
    if os.path.isfile('game_state.json'):
        with open("game_state.json", "r") as infile:
            params = dict(json.load(infile))
        return GameDataHandler(params)
    else:
        return GameDataHandler(params={"catching": False, "message": "", "last_moviemon": "", "catched_moviemon": 0})


def get_slots_info():
    if os.path.isfile('slots_state.json'):
        with open("slots_state.json", "r") as infile:
            slots = dict(json.load(infile))
    else:
        slots = {"slotA": "Free", "slotB": "Free", "slotC": "Free", "picked": 0}
        with open("slots_state.json", "w") as outfile:
            json.dump(slots, outfile)
    return slots


def save_game_to_file(pick, slots):
    tmp_dict = {0: "A", 1: "B", 2: "C"}
    pick = tmp_dict[pick]
    if os.path.isfile('game_state.json'):
        with open("game_state.json", "r") as infile:
            params = dict(json.load(infile))
        with open("slot" + pick + ".json", "w") as outfile:
            json.dump(params, outfile)
        slots["slot" + pick] = str(params["catched_moviemon"]) + " / " + str(params["all_moviemon"]) + " status"
        print(slots)
        with open("slots_state.json", "w") as outfile:
            json.dump(slots, outfile)


def load_game_from_file(pick, slots):
    tmp_dict = {0: "A", 1: "B", 2: "C"}
    pick = tmp_dict[pick]
    if os.path.isfile("slot" + pick + ".json"):
        with open("slot" + pick + ".json", "r") as infile:
            params = dict(json.load(infile))
        with open("game_state.json", "w") as outfile:
            json.dump(params, outfile)
        print("done")
        return redirect("../../worldmap")
    else:
        return redirect("/options/load_game")

