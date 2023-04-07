from flask import Flask, jsonify
import json,requests

app = Flask(__name__)

@app.route('/api1')
def api1():
    # define your logic to get data here
    data = {"message": "Hello from API 1!"}
    
    return jsonify(data)

@app.route('/api2')
def api2():
    # define your logic to get data from api1 here
    response = requests.get('http://localhost:5000/api1')
    print(response)
    try:
        data = response.json()
        message = "Hello from API 1! " + data['message']
        status = data['status']
    except KeyError:
        message = "Error: Invalid response from API 2"
        status = "error"
     # return the response as JSON
    return jsonify({'status': status, 'message': message})
    # data = response.json()
    # data["message"] = "Hello from API 2! " + data["message"]
    # return jsonify(data)

@app.route('/api3')
def api3():
    # define your logic to get data from api1 here
    response = requests.get('http://localhost:5002/api2')
    print(response)
    data = response.json()
    data["message"] = "Hello from API 3! " + data["message"]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
