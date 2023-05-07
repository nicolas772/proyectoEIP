Librerias:

- Stomp (pip install stomp.py)
- keyboard (pip install keyboard)

Para que pueda correr:

1) En un CMD, correr el servidor de ActiveMQ
	- Dirigirse al directorio donde se encuentra la carpeta de ActiveMQ
	- ejecutar: bin\activemq start
	- IMPORTANTE: se debe tener ya creada una cola en ActiveMQ llamada 'queue_sensor'

2) En otro CMD, correr el script del consumidor de queue_sensor:
	- Dirigirse al directorio proyectoEIP
	- ejecutar: python consumer_queue_sensor.py

3) En otro CMD, correr el script de la app principal:
	- Dirigirse al directorio proyectoEIP
	- ejecutar: python __main__.py