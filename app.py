import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Bem Vindo!!!"

@app.route('/comovai')
def hello():
    return 'Melhor Agora!!!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
