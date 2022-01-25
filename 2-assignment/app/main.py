from flask import Flask, render_template, request, jsonify
from phone_network_finder import find_phone_network

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/postNumber", methods=['POST'])
def post_number():
    if request.method == 'POST':
        phoneNumber = request.form['phoneNumber']
        relation_ship = find_phone_network(phoneNumber)
        return jsonify(relation_ship)


if __name__ == "__main__":
    app.run(debug=True)
