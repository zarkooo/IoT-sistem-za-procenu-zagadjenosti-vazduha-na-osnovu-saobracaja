from flask import Flask,render_template
from firebase import firebase
from bs4 import BeautifulSoup

firebase = firebase.FirebaseApplication('https://iot-brojac-default-rtdb.firebaseio.com/',None)

result = firebase.get('/IoT-Brojac/Vale', None)
app = Flask(__name__,template_folder='template')

broj = int(result)


@app.route("/")
def index():
     return render_template('index.html',variable = broj)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
