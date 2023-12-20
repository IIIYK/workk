from flask import Flask

app = Flask(__name__)

@app.route('/api/my', methods=['GET'])
def get_hello():
    return 'Hello, world!'

if __name__ == '__main__':
    app.run(debug=True)

  