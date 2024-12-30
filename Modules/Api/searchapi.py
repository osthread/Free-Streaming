from requests import get 

class Search:
    def __init__(self):
        self.headers = {"accept": "application/json", "Authorization": "API-Key"}
 
    def check_media(self, results):
        invalid_movies_ids = set()
        for result in results:
            response = get(f"https://stream.sanction.tv/embed/{result['media_type']}/{result['id']}") 
            if response.status_code == 404:
                invalid_movies_ids.add(result["id"])

        return invalid_movies_ids
        
    def check_movie(self, media_type, video_id):
        response = get(f"https://api.themoviedb.org/3/{media_type}/{video_id}", headers=self.headers).json()

        overview = response.get("overview")
        title = response.get("original_title" if media_type == "movie" else "name")
        thumbnail = response.get("poster_path")

        video_url = f"https://stream.sanction.tv/embed/{media_type}/{video_id}"
        check_res = get(video_url)
        if check_res.status_code != 200:
            video_url = video_url.replace("vidsrc.me", "vidsrc.cc")

        return video_url, overview, title, thumbnail
    
    def modified_results(self, original_results, invalid_movies_ids):
        required_keys = ['id', 'title', 'overview', 'poster_path', 'media_type','popularity', 'release_date']
        modified_and_valid_results = []

        for item in original_results:
            if item['id'] in invalid_movies_ids:
                continue

            if 'name' in item:
                item['title'] = item.pop('name')
    
            if 'first_air_date' in item:
                item['release_date'] = item.pop('first_air_date')
    
            if all(key in item and item[key] for key in required_keys):
                modified_and_valid_results.append(item)
    
        return modified_and_valid_results

    def get_upcoming(self):
        response = get("https://api.themoviedb.org/3/movie/upcoming?language=en-US", headers=self.headers)
        upcoming_movies = response.json().get('results', [])
        return upcoming_movies

    def get_trending_movies(self): 
        response = get("https://api.themoviedb.org/3/trending/movie/day?language=en-US", headers=self.headers)
        original_results = response.json().get('results', [])
        invalid_movies_ids = self.check_media(original_results)
        modified_and_valid_results = self.modified_results(original_results, invalid_movies_ids)
        return modified_and_valid_results

    def get_trending_tv(self):
        response = get("https://api.themoviedb.org/3/trending/tv/day?language=en-US", headers=self.headers)
        original_results = response.json().get('results', [])
        invalid_movies_ids = self.check_media(original_results)
        modified_and_valid_results = self.modified_results(original_results, invalid_movies_ids)
        return modified_and_valid_results

    def search_results(self, query):
        response = get(f"https://api.themoviedb.org/3/search/multi?query={query}", headers=self.headers)
        original_results = response.json().get('results', [])
        invalid_movies_ids = self.check_media(original_results)
        modified_and_valid_results = self.modified_results(original_results, invalid_movies_ids)
        return modified_and_valid_results
