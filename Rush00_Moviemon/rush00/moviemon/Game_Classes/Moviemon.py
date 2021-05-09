import requests

API_KEY = '580175a1'
DATA_API = 'http://www.omdbapi.com/'


class Moviemon:

    def __init__(self, imdb_id):
        params = {
            'apikey': API_KEY,
            'i': imdb_id,
        }
        response = requests.get(DATA_API, params)
        if response.status_code != 200:
            raise requests.HTTPError('API call failed')
        data = response.json()
        self.movie_id = imdb_id
        self.name = data['Title']
        self.poster = data['Poster']
        self.director = data['Director']
        self.year = data['Year']
        self.rating = data['imdbRating']
        self.synopsis = data['Plot']
        self.actors = data['Actors']
        self.strength = float(self.rating)

    def __str__(self):
        return (f'name = {self.name}'
                + f'poster url = {self.poster}'
                + f'director = {self.director}'
                + f'year = {self.year}'
                + f'rating = {self.rating}'
                + f'synopsis = {self.synopsis}'
                + f'actors = {self.actors}')


if __name__ == '__main__':
    TEST_ID = 'tt0103874'  # Dracula
    m = Moviemon(TEST_ID)
    print(m)
