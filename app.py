from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

movies = [
    {
        'id': 1,
        'title': 'Romeu e Julieta',
        'imdb_rate': 8.1,
        'description': 'blablabla lorem ipsum'
    },
    {
        'id': 2,
        'title': 'Cruzao e Tiago, a super dupla dinâmica',
        'imdb_rate': 100000,
        'description': 'blablabla2 lorem2 ipsum2'
    },
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/movies/all', methods=['GET'])
def get_all_movies():
    return jsonify(movies)


@app.route('/api/movies/', methods=['GET'])
def get_movie():
    movie_id = int(request.args.get('id'))
    for movie in movies:
        if movie['id'] == movie_id:
            return jsonify(movie)

    return jsonify({'error': 'could not find movie'})


if __name__ == '__main__':
    app.run(debug=True)
