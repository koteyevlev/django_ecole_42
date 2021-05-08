from django.shortcuts import render


def index(request):
    return render(request, "title_screen.html")


def options(request):
    return render(request, "options.html")


def load_game(request):
    return render(request, "load_game.html")


def save_game(request):
    return render(request, "save_game.html")


def worldmap(request):
    return render(request, "worldmap.html", {"rows": range(10), "columns": range(10),
                                             "player_col": 5, "player_row": 4})


def battle(request, id):
    return render(request, "battle.html")


def detail(request, id):
    id += 1
    return render(request, "detail.html")


def moviedex(request):
    return render(request, "moviedex.html")

