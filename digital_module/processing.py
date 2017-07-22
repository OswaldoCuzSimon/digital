from cassandra.cluster import Cluster
import datetime

class Processing:
	def __init__(self,url):
		self.cluster = Cluster([url])
		self.session = self.cluster.connect('digital')
	def save_latido(self,data):
		for row in data:
			self.session.execute("INSERT INTO sensor (uid,date,measure) VALUES (%s,%s,%d)", values)

	def dummy_save_latido(self):
		for i in range(20):
			data = {
				'uid': '1',
				'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
				'measure': 85 
			}
			values = (data['uid'],data['date'],data['measure'])
			self.session.execute("INSERT INTO sensor (id_sensor,uid,date,measure) VALUES (now(),%s,%s,%s)", values)
