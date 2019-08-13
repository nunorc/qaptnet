
from flask import Flask, jsonify, request
from flask_cors import CORS

from qaptnet import qaptnet

ptnet = qaptnet()

app = Flask(__name__)
CORS(app)

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    return jsonify({'answer': ptnet.query(context  = data['context'],
                                          question = data['question'])})

@app.route('/', methods=['GET'])
def _root():
  return 'qaptnet-api'

if __name__ == '__main__':
    app.run(port=7788)

