from flask import Flask, jsonify
import random

app = Flask(__name__)

cpf = [
    "008.789.145-88",
    "007.589.175-99.",
    "006.458.774-52",
    "007.159.788-36",
]

@app.route('/cpf', methods=['GET'])
def get_conselho():
    conselho = random.choice(cpf)
    return jsonify({'cpf': cpf})

if __name__ == '__main__':
    app.run(debug=True)
