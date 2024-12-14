from flask import Flask

app = Flask(__name__)

@app.route('/flag', methods=['GET'])
def get_flag():
    return "WLUG{121203}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
