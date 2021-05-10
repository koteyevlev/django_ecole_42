import psycopg2
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def init(request):
    sql_request = """
    CREATE TABLE IF NOT EXISTS ex04_movies (
    title varchar(64) UNIQUE NOT NULL,
    episode_nb serial PRIMARY KEY,
    opening_crawl text,
    director varchar(32) NOT NULL,
    producer varchar(128) NOT NULL,
    release_date date NOT NULL
    )
    """
    return execute_request_to_sql(sql_request)


def populate(request):
    sql_request = "INSERT INTO ex04_movies (episode_nb, title, director, producer, release_date) VALUES "
    data = [
    (1, 'The Phantom Menace', 'George Lucas', 'Rick McCallum', '1999-05-19'),
    (2, 'Attack of the Clones', 'George Lucas', 'Rick McCallum', '2002-05-16'),
    (3, 'Revenge of the Sith', 'George Lucas', 'Rick McCallum', '2005-05-19'),
    (4, 'A New Hope', 'George Lucas', 'Gary Kurtz, Rick McCallum', '1977-05-25'),
    (5, 'The Empire Strikes Back', 'Irvin Kershner', 'Gary Kurtz, Rick McCallum', '1980-05-17'),
    (6, 'Return of the Jedi', 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum', '1983-05-25'),
    (7, 'The Force Awakens', 'J. J. Abrams', 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', '2015-12-11')
    ]
    result = []
    for film in data:
        try:
            conn = psycopg2.connect(
                database="djangotraining",
                host="localhost",
                user='djangouser',
                password='secret'
            )
            curr = conn.cursor()
            curr.execute(sql_request + str(film))
            conn.commit()
            conn.close()
            result.append(film[1] + "OK,")
        except Exception as e:
            result.append("error - " + str(film[1]) + ",")
    print(result)
    return HttpResponse(result)


def display(request):
    try:
        conn = psycopg2.connect(
            database="djangotraining",
            host="localhost",
            user='djangouser',
            password='secret'
        )
        curr = conn.cursor()

        curr.execute(""" SELECT * From ex04_movies """)
        response = curr.fetchall()

        conn.close()
        if len(response) == 0:
            response = ["No data available"]
        return render(request, "display_ex04.html", {"data": response})
    except Exception as e:
        return HttpResponse("No data available")


def remove(request):
    try:
        conn = psycopg2.connect(
            database="djangotraining",
            host="localhost",
            user='djangouser',
            password='secret'
        )
        curr = conn.cursor()
        if request.method == "POST":
            curr.execute(" Delete From ex04_movies where episode_nb = %s", [int(request.POST["movies"])])
            conn.commit()
            print("removed", request.POST["movies"])


        curr.execute(""" SELECT * From ex04_movies """)
        response = curr.fetchall()

        conn.close()
        if len(response) == 0:
            raise Exception()
        return render(request, "remove.html", {"data": response})
    except Exception as e:
        print(e)
        return HttpResponse("No data available")


def execute_request_to_sql(sql_request):
    try:
        conn = psycopg2.connect(
            database="djangotraining",
            host="localhost",
            user='djangouser',
            password='secret'
        )
        curr = conn.cursor()

        curr.execute(sql_request)
        conn.commit()
        conn.close()
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(e)
