from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        'message': 'Welcome to the Flask API!',
        'status': 'success'
    })

@app.route('/home',methods=["GET"])
def home():
    return jsonify({
        'message': 'Welcome to the Flask API!',
        'status': 'success'
    })

if __name__ == '__main__':
    app.run(debug=True) 