from waitress import serve
from flask_cors import CORS
from flask import Flask, request, render_template, abort

from Modules.Api.searchapi import Search

import requests

class Streaming:
    def __init__(self):
        self.app = Flask(__name__)
        self.routes()
        self.sapi = Search()
        self.headers = {"accept": "application/json", "Authorization": "API-Key"}

    def check_movie(self, media_type, video_id):
        response = requests.get(f"https://api.themoviedb.org/3/{media_type}/{video_id}", headers=self.headers).json()

        overview = response.get("overview")
        title = response.get("original_title" if media_type == "movie" else "name")
        thumbnail = response.get("poster_path")

        video_url = f"https://vidsrc.to/embed/{media_type}/{video_id}"
        check_res = requests.get(video_url)
        if check_res.status_code != 200:
            video_url = video_url.replace("vidsrc.to", "vidsrc.xyz")

        return video_url, overview, title, thumbnail
    
    def routes(self):
        @self.app.route('/watch/<key>')
        def index(key):
            return render_template('index.html', movies=self.sapi.get_trending_movies(), tv=self.sapi.get_trending_tv(), upcoming=self.sapi.get_upcoming())

        @self.app.route('/watch/search')
        def searchresults():
            query = request.args.get('query')
            search = self.sapi.search_results(query)
            return render_template('results.html', search=search)
            
        @self.app.route('/watch/<media_type>/<video_id>')
        def watch_video(media_type, video_id):
            if media_type not in ["movie", "tv"]: 
                abort(404)

            response = self.check_movie(media_type, video_id)

            return render_template('watch.html', video_url=response[0], title=response[2], overview=response[1], thumbnail=response[3])

    def run(self):
        CORS(self.app)
        serve(self.app, host="127.0.0.1", port=9999)

if __name__ == '__main__':
    Trinix = Streaming()
    Trinix.run()
