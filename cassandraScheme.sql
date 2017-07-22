CREATE KEYSPACE digital WITH  replication = {'class':'SimpleStrategy','replication_factor':1};
use digital;
CREATE TABLE sensor(
	id_sensor timeuuid PRIMARY KEY,
	sensor_type int,
	uid varchar,
	date timestamp,
	measure int
);

CREATE INDEX ON sensor( uid );
CREATE INDEX ON sensor( sensor_type );