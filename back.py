from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "This route is not used."

@app.route('/favicon.ico')
def favicon():
    return "This route is not used."

@app.route('/hello', methods=['POST'])
def hello():
    name = request.form.get('name')
    return "This route is not used."

if __name__ == '__main__':
    print('Message to be printed without using the interface')
