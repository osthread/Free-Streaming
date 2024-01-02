import requests 

class Search:
    def __init__(self):
        self.headers = {"accept": "application/json", "Authorization": self.get_token()}

    def get_token(self):
        tokens = ["Api-Keys"]

        for t in tokens:
            return t

    def get_Upcoming(self):
        url = "https://api.themoviedb.org/3/movie/upcoming?language=en-US"
        response = requests.get(url, headers=self.headers)
        upcoming = response.json().get('results', [])
        return upcoming

    def get_trending_movies(self):
        url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"
        response = requests.get(url, headers=self.headers)
        trending_movies = response.json().get('results', [])
        return trending_movies

    def get_trending_tv(self):
        url = "https://api.themoviedb.org/3/tv/popular?language=en-US&page=1"
        response = requests.get(url, headers=self.headers)
        trending_tv = response.json().get('results', [])
        return trending_tv

    def search_results(self, query):
        url = f"https://api.themoviedb.org/3/search/multi?query={query}"

        response = requests.get(url, headers=self.headers)

        data = response.json()

        original_results = data.get('results', [])

        modified_and_valid_results = []

        required_keys = [
            'id', 'title', 'overview', 'poster_path', 'media_type',
            'popularity', 'release_date']

        for item in original_results:
            if 'name' in item:
                item['title'] = item.pop('name')

            if 'first_air_date' in item:
                item['release_date'] = item.pop('first_air_date')

            if all(key in item and item[key] for key in required_keys):
                modified_and_valid_results.append(item)

        return modified_and_valid_results