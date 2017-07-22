from flask import Flask
from flask import request
from flask import jsonify
from digital_module.processing import Processing

URL_DB = 'localhost'
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World'

@app.route('/api/v1/save_data/<sensor>/',methods=["POST"])
def save_data(sensor):
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

if __name__ == '__main__':
	app.run(debug=True)
