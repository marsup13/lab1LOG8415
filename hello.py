from flask import request, jsonify, Flask
from requests import get 
app = Flask(__name__)

@app.route('/<path:text>', methods=['GET']) 
def my_app(text):
    if text.startswith('cluster'):
        return {
            "Instance ID": get('http://169.254.169.254/latest/meta-data/instance-id').content.decode('utf8'),
        }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
