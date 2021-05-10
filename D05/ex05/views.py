import psycopg2
from django.http import HttpResponse
from django.shortcuts import render
from .models import Movies

def populate(request):
    data = [
            (1, 'The Phantom Menace', 'George Lucas', 'Rick McCallum', '1999-05-19'),
            (2, 'Attack of the Clones', 'George Lucas', 'Rick McCallum', '2002-05-16'),
            (3, 'Revenge of the Sith', 'George Lucas', 'Rick McCallum', '2005-05-19'),
            (4, 'A New Hope', 'George Lucas', 'Gary Kurtz, Rick McCallum', '1977-05-25'),
            (5, 'The Empire Strikes Back', 'Irvin Kershner', 'Gary Kurtz, Rick McCallum', '1980-05-17'),
            (6, 'Return of the Jedi', 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum', '1983-05-25'),
            (7, 'The Force Awakens', 'J. J. Abrams', 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', '2015-12-11')
    ]
    res = []
    for film in data:
        try:
            movie = Movies(
                episode_nb=film[0],
                title=film[1],
                director=film[2],
                producer=film[3],
                release_date=film[4]
            )
            movie.save(force_insert=True)
            res.append(film[1] + " OK,")
        except Exception as e:
            res.append(film[1] + " failed,")
    return HttpResponse(res)



def display(request):
    try:
        data = list(Movies.objects.all())
        print(type(data[0]))
        return render(request, "display_ex05.html", {"data": data})
    except Exception as e:
        print(e)
        return HttpResponse("No data available")



def remove(request):
    try:
        if request.method == "POST":
            del_movie = Movies.objects.filter(episode_nb=int(request.POST["movies"]))
            del_movie.delete()
            print("removed", request.POST["movies"])

        data = list(Movies.objects.all())
        if len(data) == 0:
            raise Exception()
        return render(request, "remove_ex05.html", {"data": data})
    except Exception as e:
        print(e)
        return HttpResponse("No data available")

