from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/api1')
def api1():
    # define your logic to get data here
    data = {"message": "Hello from API 1!"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
