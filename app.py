from flask import Flask, request, jsonify
from flask_cors import CORS
from backend import generate_financial_report

app = Flask(__name__)
CORS(app)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    query = data.get("query")
    result = generate_financial_report(query)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
