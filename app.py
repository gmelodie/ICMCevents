from flask import Flask, render_template, request, jsonify
import scrapper

app = Flask(__name__)

easter_egg = {
        'authors': 'Gabriel Cruz and Tiago Miranda',
        'professor': 'Jó Ueyama',
        'teaching assistant': 'Thiago Costa',
        'flag': 'redesmoveis{3h_d4h0r4}'
}

@app.route('/easter_egg')
def render_easter_egg():
    return jsonify(easter_egg)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/events/all', methods=['GET'])
def get_all_icmc_events():
    return jsonify(scrapper.get_icmc_events())


if __name__ == '__main__':
    app.run(debug=True)
