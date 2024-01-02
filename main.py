from waitress import serve
from flask_cors import CORS
from flask import Flask, request, jsonify, render_template

from Modules.Api.searchapi import Search

import os, string, requests

class Streaming:
    def __init__(self):
        self.app = Flask(__name__)
        self.routes()
        self.sapi = Search()
        self.headers = {"accept": "application/json", "Authorization": self.get_token()}

    def get_token(self):
        tokens = ["Api_Keys"]

        for t in tokens:
            return t

    def routes(self):
        @self.app.route('/')
        def index():
            return render_template('index.html', movies=self.sapi.get_trending_movies(), tv=self.sapi.get_trending_tv(), upcoming=self.sapi.get_Upcoming())

        @self.app.route('/search')
        def searchresults():
            query = request.args.get('query')
            search = self.sapi.search_results(query)
            return render_template('results.html', search=search)

        @self.app.route('/watch/<media_type>/<video_id>')
        def watch_video(media_type, video_id):
            response = requests.get(f"https://api.themoviedb.org/3/{media_type}/{video_id}", headers=self.headers).json()
            overview = response.get("overview")
            if media_type == "movie":
                video_url = f"https://vidsrc.to/embed/movie/{video_id}"
                title = response.get("original_title")
                thumbnail = response.get("poster_path")

            elif media_type == "tv":
                video_url = f"https://vidsrc.to/embed/tv/{video_id}"
                title = response.get("name")
                thumbnail = response.get("poster_path")
            
            return render_template('watch.html', video_url=video_url, title=title, overview=overview, thumbnail=thumbnail) 

        @self.app.route('/watch/anime/<video_id>')
        def watch_anime(video_id):
            response = requests.get(f"https://api.themoviedb.org/3/tv/{video_id}", headers=self.headers).json()
            overview = response.get("overview")
            video_url = f"https://vidsrc.me/embed/tv?tmdb={video_id}"
            title = response.get("name")
            thumbnail = response.get("poster_path")
            
            return render_template('watch.html', video_url=video_url, title=title, overview=overview, thumbnail=thumbnail) 

    def run(self):
        CORS(self.app)
        serve(self.app, host="0.0.0.0", port=9999)

if __name__ == '__main__':
    Trinix = Streaming()
    Trinix.run()
