from django.http import HttpResponse
from django.shortcuts import render
import psycopg2

# Create your views here.

def init(request):
    try:
        conn = psycopg2.connect(
            database="djangotraining",
            host="localhost",
            user='djangouser',
            password='secret'
        )
        curr = conn.cursor()

        curr.execute(
            """
            CREATE TABLE IF NOT EXISTS ex00_movies (
            title varchar(64) UNIQUE NOT NULL,
            episode_nb serial PRIMARY KEY,
            opening_crawl text,
            director varchar(32) NOT NULL,
            producer varchar(128) NOT NULL,
            release_date date NOT NULL
            )
            """
        )
        conn.commit()
        conn.close()
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(e)

