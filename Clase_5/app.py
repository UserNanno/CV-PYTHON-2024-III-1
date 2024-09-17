from flask import Flask, jsonify, request # JSON
from bs4 import BeautifulSoup
import json
import requests

# Inicialización de la aplicación FLASK

app = Flask(__name__)

# Definir la ruta 

@app.route('/amazon', methods=["GET"])
def amazon():
    data = json.loads(request.data) # data.astype = Dict
    headers = {'Fuser': 'An', 'user-agent':'an'}
    if 'palabra' in data:
        if len(data['palabra']) == 0:
            return jsonify({"respuesta": "palabra vacía"})
        
        url = "https://www.amazon.com/s?k={}".format(data['palabra'])
        r = requests.get(url, headers=headers)
    
    # PROCESAMIENTO DEL HTML
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, 'html.parser')
            urls = soup.find('div', attrs={"class":"s-main-slot s-result-list s-search-results sg-row"}).find_all('a', attrs={"class":"a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"})
            urls = ["https://www.amazon.com/" + i.get('href') for i in urls[:5]]
            return jsonify({"data": urls})
        return jsonify({"respuesta":"Falló"})
    return jsonify({"respuesta":"Palabra no enviada desde el body"})

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")  