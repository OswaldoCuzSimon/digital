# Sleep predictor end client
# Copyright (c) Andreas Urbanski, 2017
from .predict import predict_sleep_time_and_quality
from .build import minutes_to_hourmins
import datetime
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

def predict(h, m, w):
	date = datetime.datetime.today().replace(hour=h, minute=m) + datetime.timedelta(hours=(24 * w))

	p = predict_sleep_time_and_quality(date)

	sleep_time = list(minutes_to_hourmins(int(p[0])))
	sleep_quality = p[1] * 100.0

	wake_time = date + datetime.timedelta(hours=sleep_time[0], minutes=sleep_time[1])

	text = """Tu bebe dormira {0} horas {1} minutos, 
	Y se despertara en {2} con una calidad de sueno del  {3:.1f}%""".format(
	    sleep_time[0],
	    sleep_time[1],
	    wake_time.strftime('%A, %d/%m aproximadamente a las %H:%M'),
	    sleep_quality
	)
	print(text)
	result = {
		"sleep_time": str(sleep_time[0])+":"+str(sleep_time[1]),
		"wake_date": wake_time.strftime('%A, %d-%m'),
		"wake_time": wake_time.strftime('%H:%M'),
		"message": text
	}
	return result

#h, m = map(int, (input('Hora de ir a la cama? (formato=HH:MM) ') or '00:00').split(':'))
#w = int(input('Dia de la semana (default=0)? ') or 0)
#predict(h, m, w)
