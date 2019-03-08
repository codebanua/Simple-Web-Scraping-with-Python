from flask import Flask,request
from example import persamaankata
import json, time

app = Flask(__name__)
pk = persamaankata()

@app.route('/')
def hello_world():
    return 'its work!'

@app.route('/search')
def search():
  try:
    start = time.time()
    text = request.args.get('kata', default = 'belajar', type = str)
    resp = pk.search(text)
    elapsed_time = time.time() - start
    ret = {"code":"200","result":resp,"responsetime":str(elapsed_time)}
    return json.dumps(ret)
  except Exception as E:
  	ret = {"code":"500","result":str(E)}
  	return json.dumps(ret)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)