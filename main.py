from flask import Flask, jsonify
import logic
app = Flask(__name__)

@app.route('/api')
def hello_world():
    return 'Api Entry Point (add documentation here or something)!'

@app.route('/api/states')
def get_states():
    return jsonify(states=logic.get_states())



if __name__ == '__main__':
    app.run(host='0.0.0.0')
