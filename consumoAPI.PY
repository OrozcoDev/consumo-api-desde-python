from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    urlBase = 'https://dragonball-api.com/api/characters?limit=100'
    data = requests.get(urlBase).json()  # Convertimos directamente la respuesta a JSON
    return render_template('/index.html', personajes=data)  # Pasamos los datos directamente a la plantilla

if __name__ == '__main__':
    app.run(debug=True)