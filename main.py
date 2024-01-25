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

    def routes(self):
        @self.app.route('/watch/')
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

            response = self.sapi.check_movie(media_type, video_id)

            return render_template('watch.html', video_url=response[0], title=response[2], overview=response[1], thumbnail=response[3])

    def run(self):
        CORS(self.app)
        serve(self.app, host="127.0.0.1", port=9999)

if __name__ == '__main__':
    Trinix = Streaming()
    Trinix.run()
