# Sleep predictor end client
# Copyright (c) Andreas Urbanski, 2017
from predict import predict_sleep_time_and_quality
from build import *
import datetime
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

h, m = map(int, (input('Hora de ir a la cama? (formato=HH:MM) ') or '00:00').split(':'))
w = int(input('Dia de la semana (default=0)? ') or 0)

date = datetime.datetime.today().replace(hour=h, minute=m) + datetime.timedelta(hours=(24 * w))

p = predict_sleep_time_and_quality(date)

sleep_time = list(minutes_to_hourmins(int(p[0])))
sleep_quality = p[1] * 100.0

wake_time = date + datetime.timedelta(hours=sleep_time[0], minutes=sleep_time[1])

print ('\nTu bebe dormira {0} horas {1} minutos, Y se despertara en \n\t{2}\n\t\tcon una calidad de sueno del  {3:.1f}%'.format(
    sleep_time[0],
    sleep_time[1],
    wake_time.strftime('%A, %d/%m aproximadamente a las  %H:%M'),
    sleep_quality
)
)