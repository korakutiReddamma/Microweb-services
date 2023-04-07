import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api2')
def api2():
    # define your logic to get data from api1 here
    response = requests.get('http://localhost:5000/api1')
    print(response)
    data = response.json()
    data["message"] = "Hello from API 2! " + data["message"]
    return jsonify(data)

if __name__ == '__main__':
     app.run(debug=True, port=5001)
