# CRUD Pokemon DAL (Data Access Layer)

from flask import Flask, render_template, jsonify
import json
import random
import os
import socket
import requests

app = Flask(__name__)

def get_server_info():
    # Get server IP
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    
    # Get Availability Zone from AWS metadata
    try:
        az_response = requests.get('http://169.254.169.254/latest/meta-data/placement/availability-zone', timeout=1)
        az = az_response.text
    except:
        az = "Not available (not running in AWS)"
    
    return {
        'ip': ip,
        'az': az
    }

def get_random_pokemon():
    json_path = os.path.join(os.path.dirname(__file__), 'AllPokemons.json')
    with open(json_path, 'r') as file:
        pokemons = json.load(file)
        return random.choice(pokemons)

@app.route('/')
def index():
    random_pokemon = get_random_pokemon()
    server_info = get_server_info()
    return render_template('index.html', pokemon=random_pokemon, server_info=server_info)

@app.route("/health")
def health_check():
    return "OK", 200

@app.route('/random_pokemon', methods=['GET'])
def random_pokemon():
    pokemon = get_random_pokemon()
    return jsonify(pokemon)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

    # app.run(debug=True)
