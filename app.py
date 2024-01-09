from flask import Flask, request, jsonify, render_template
import datetime


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/heure')
def heure():
    date_heure = datetime.datetime.now()
    h = date_heure.hour
    m = date_heure.minute
    s = date_heure.second
    return render_template("heure.html", heure=h, minute=m, seconde=s)


# route avec parametre dans lURL
@app.route('/hello/<name>')
def hello(name):
    return f'Hello, {name}!'


#route POST pour recevoir des données en JSON et renvoyer une reponse en JSON
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json # recuperer les donnees JSON

    #effectuer une operation 
    result = {'result': data['number']* 2}

    return jsonify(result) #renvoyer la reponse JSON


##lancer l'application lorsque le script est lancer avec un terminal
if __name__ == '__main__':
    app.run(debug=True)