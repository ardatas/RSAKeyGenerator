from flask import Flask, jsonify
from rsa import RSA

app = Flask(__name__)


@app.route("/index")
def createKeyPairs():

    keys = RSA.generate_keypair()








