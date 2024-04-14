from flask import Flask
app = Flask(__name__)
  

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/submit', actions=["POST","GET"])
def hello_world_submit():
    return 'Hello World Submit'

if __name__ == '__main__':
    app.run()
