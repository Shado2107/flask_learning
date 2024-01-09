from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/')
def home():
    return 'Bienvenue sur l\'API Flask'

# route avec parametre dans lURL
@app.route('/hello/<name>')
def hello(name):
    return f'Hello, {name}!'


#route POST pour recevoir des données en JSON et renvoyer une reponse en JSON
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json # recuperer les donnees JSON

    #effecxtuer une operation 
    result = {'result': data['number']* 2}

    return jsonify(result) #renvoyer la reponse JSON


if __name__ == '__main__':
    app.run(debug=True)