from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to My Flask API App!</h1>"

@app.route("/get-fact")
def get_fact():
    response = requests.get("https://catfact.ninja/fact")
    data = response.json()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
def home():
    url='https://catfact.ninja/fact'
    response=requests.get(url)
    data=response.json()
    print(data)
    return "<p>{data}</p>"

@app.route("catbreeds")
def catbreeds():
    url='https://catfact.ninja/breeds?limit={3}'
    response=requests.get(url)
    data=response.json()
    return jsonify(data)
