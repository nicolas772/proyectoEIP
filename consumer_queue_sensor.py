import stomp
import time

class MyListener(stomp.ConnectionListener):
    def __init__(self, conn):
        self.conn = conn

    def on_error(self, frame):
        print('received an error "%s"' % frame.body)

    def on_message(self, frame):
        print('received a message "%s"' % frame.body)
        if frame.body == 'off':
            print('\n', 'Cerrando Cola.')
            time.sleep(1)
            self.conn.disconnect()
    def on_disconnected(self):
        print('disconnected')
# Configura tus credenciales y dirección del servidor ActiveMQ

activemq_server = "localhost"
activemq_port = 61613  # Por defecto, ActiveMQ utiliza el puerto 61613 para STOMP
activemq_username = "admin"
activemq_password = "admin"
queue_name = "/queue/queue_sensor"

# Conectar al servidor ActiveMQ

connection = stomp.Connection([(activemq_server, activemq_port)])
connection.set_listener("", MyListener(connection))
#connection.start()
connection.connect(login=activemq_username, passcode=activemq_password, wait=True)

# Suscribirse a la cola

connection.subscribe(destination=queue_name, id=1, ack="auto")

# Esperar mensajes

print("[queue_sensor] Esperando mensajes... presiona Ctrl+C para salir")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass

# Desconectar del servidor ActiveMQ
connection.disconnect()