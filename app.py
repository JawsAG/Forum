from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/captions', methods=['POST'])
def get_captions():
    data = request.get_json()
    youtube_link = data['youtubeLink']

    # Placeholder for fetching captions, you need to implement this
    captions = fetch_captions(youtube_link)

    return jsonify(captions)

@app.route('/search', methods=['POST'])
def search_keywords():
    data = request.get_json()
    youtube_link = data['youtubeLink']
    keywords = data['keywords'].split(',')

    # Placeholder for fetching captions and searching keywords, you need to implement this
    captions = fetch_captions(youtube_link)
    search_results = search_in_captions(captions, keywords)

    return jsonify(search_results)

def fetch_captions(youtube_link):
    # Placeholder for fetching captions, you need to implement this
    captions = ["Caption 1", "Caption 2", "Caption 3"]  # Example captions
    return captions

def search_in_captions(captions, keywords):
    # Placeholder for searching keywords in captions, you need to implement this
    search_results = {keyword: captions.count(keyword) for keyword in keywords}
    return search_results

if __name__ == '__main__':
    app.run(debug=True)
