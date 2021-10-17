from flask import Flask, json, request
from checker import main

app = Flask(__name__)

@app.route("/reg/check")
def hello_world():
    name = request.args.get('name')
    result = main(name)
    return json.dumps(result)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3042)