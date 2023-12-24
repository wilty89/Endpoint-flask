from flask import Flask, json, jsonify, render_template,request,make_response
from flask_cors import CORS
from time import sleep;
import datetime
from os import environ
import payment

variable = environ.get('DB_URL')

app = Flask(__name__)
CORS(app)

"""
Webs de interés:
- Módulo OpenAI: https://github.com/openai/openai-python
- Documentación API ChatGPT: https://platform.openai.com/docs/api-reference/chat
- Typer: https://typer.tiangolo.com
- Rich: https://rich.readthedocs.io/en/stable/
"""
@app.errorhandler(404)
def page_not_found(error):
    return("WRONG_URL. Use the correct format:")

@app.route('/')
def home():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())

@app.route('/about/')
def about():
    return render_template('about.html')

    
@app.route("/hello")
def welcome():
    return "Hello world!"+ variable

@app.route('/test', methods=['GET'])
def test():
  return make_response(jsonify({'message': 'test route'}), 200)

@app.route('/payment')  
def payments():  
    webhook_payload_json = json.dumps(payment.get_payment())  
    return webhook_payload_json  


@app.route('/numbers/')
def print_list():
    return jsonify(list(range(5)))  


@app.route('/person/')
def hello():
    return jsonify({'name':'Jimit',
                    'address':'India'})


incomes = [
    { 'description': 'salary', 'amount': 5000 }
]
@app.route('/incomes', methods=['POST'])
def add_income():
    incomes.append(request.get_json())
    return incomes, 201


@app.route('/api/products')
def getProducts():
    sleep(1)
    products= {'data':[
        {
            'id': 1,
            'productName': 'Macbook Air M1 2020 256GB',
            'brand': 'Apple Inc.',
            'model': 'MAL920A',
            'description': 'Macbook Air procesador M1 7 cores CPU 8 Cores GPU 8GB ram 256GB SSD ',
            'unitPrice': 950.00,
            'thumbnail': 'https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/macbook-air-space-gray-config-201810?wid=1078&hei=624&fmt=jpeg&qlt=90&.v=1633033424000',
            'macType':'Macbook Air'
        },
        {
            'id': 2,
            'productName': 'Macbook Air M1 2020 512GB',
            'brand': 'Apple Inc.',
            'model': 'MAL921A',
            'description': 'Macbook Air procesador M1 8 cores CPU 8 Cores GPU 8GB ram 512GB SSD ',
            'unitPrice': 1199.00,
            'thumbnail': 'https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/macbook-air-space-gray-config-201810?wid=1078&hei=624&fmt=jpeg&qlt=90&.v=1633033424000',
            'macType':'Macbook Air'

        },
        {
            'id': 3,
            'productName': 'Macbook PRO M1 2020 256GB',
            'brand': 'Apple Inc.',
            'model': 'MAL921A',
            'description': 'Macbook Air procesador M1 8 cores CPU 8 Cores GPU 8GB ram 256GB SSD ',
            'unitPrice': 1350.00,
            'thumbnail': 'https://m.media-amazon.com/images/I/71DIt6oIe3L._AC_SL1500_.jpg',
            'macType':'Macbook Pro'

        },
        {
            'id': 4,
            'productName': 'Macbook Pro M1 pro 16GB ram 512GB 2021',
            'brand': 'Apple Inc.',
            'model': 'MSL921A',
            'description': 'MAc studio Air procesador M1 MAX 8 cores CPU y 14 cores GPU 16GB ram 512GB SSD, pantalla XDR ',
            'unitPrice': 1950.00,
            'thumbnail': 'https://m.media-amazon.com/images/I/61vFO3R5UNL._AC_SL1500_.jpg',
            'macType':'Macbook Pro'
        },
        {
            'id': 5,
            'productName': 'MAC Studio M1 Max 2021 512GB',
            'brand': 'Apple Inc.',
            'model': 'MSL922A',
            'description': 'MAc studio Air procesador M1 MAX 10 cores CPU y 24 cores GPU 32GB ram 512GB SSD ',
            'unitPrice': 1999.00,
            'thumbnail': 'https://www.apple.com/v/mac-studio/a/images/overview/hero/static_front__fmvxob6uyxiu_large.jpg',
            'macType':'Mac Studio'
        },
        {
            'id': 6,
            'productName': 'Apple iMac 2021 - 24 pulgadas, chip Apple M1 con CPU de 8 núcleos y GPU de 7 núcleos, 8 GB de RAM, 256 GB, plata',
            'brand': 'Apple Inc.',
            'model': 'MIL921A',
            'description': '',
            'unitPrice': 1249.99,
            'thumbnail': 'https://m.media-amazon.com/images/I/61LNnZPoKPS._AC_SL1500_.jpg',
            'macType':'iMac'
        },
        {
            'id': 7,
            'productName': 'Mac Mini M1 2020 - 8Gb ram 256GB SSD',
            'brand': 'Apple Inc.',
            'model': 'MIL921A',
            'description': 'Apple Mac Mini 2020 con chip Apple M1 (8 GB de RAM, 256 GB de almacenamiento SSD)',
            'unitPrice': 669.99,
            'thumbnail': 'https://m.media-amazon.com/images/I/71pcTYT+ICL._AC_SL1500_.jpg',
            'macType':'Mac Mini'
        }

        
    ]}
    return render_template('productos.html', products=products)



if __name__ == '__main__':
    app.run(debug=True)



#python --version
#pip --version
    #pip install Flask
    #pip install -U flask-cors
    #python app.py
    #pip freeze > requirements.txt
    #pip install -r requirements.txt
    #pip list
    #docker build -t mi-aplicacion-flask .
    #docker run -p 4000:4000 mi-aplicacion-flask

    # o tambien docker compose up flask_app