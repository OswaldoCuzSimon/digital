from flask import Flask
from flask import request
from flask import jsonify
from digital_module.processing import Processing
from sleephow.sleephow import predict
URL_DB = 'localhost'
app = Flask(__name__)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

@app.route('/')
def hello_world():
	return 'Hello World'

@app.route('/api/v1/save_data/<sensor>/',methods=["POST"])
def save_data_endpoint(sensor):
	try:
		data = request.json
		if sensor == 'latido':
			process = Processing(URL_DB)
			process.dummy_save_latido()
		
		return jsonify(data)
	except Exception as e:
		app.logger.error(e)
		data = {"success": False,"error": 200}
		return jsonify(data), 200

@app.route('/api/v1/predict/',methods=["POST"])
def predict_endpoint():
	print(request.json)
	try:
		data = request.json
		time = data['time']
		day = int(data['day'])
		result = predict(int(time.split(':')[0]),int(time.split(':')[1]),day)
		return jsonify(result)
	except Exception as e:
		app.logger.error(e)
		data = {"success": False,"error": 200}
		return jsonify(data), 200
if __name__ == '__main__':
	app.run(debug=True,host= '0.0.0.0')
