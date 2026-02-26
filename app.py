from flask import Flask, jsonify, render_template
from rsa import RSA

app = Flask(__name__, static_folder="static", static_url_path="/static")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/generate", methods=["GET"])
def generate_keypair():
    public_key, private_key = RSA.generate_keypair()
    e, n = public_key
    d, _ = private_key

    return jsonify(
        {
            "public_key": {
                "e": str(e),
                "n": str(n),
            },
            "private_key": {
                "d": str(d),
                "n": str(n),
            },
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
