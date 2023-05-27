import stomp
import random
import json
import keyboard
import time
import src.conection.conection as CONN
sensores = [1,2,3,4]

class MyListener(stomp.ConnectionListener):
    def __init__(self, conn):
        self.message_body = None  # Variable para almacenar el cuerpo del mensaje
        self.conn = conn
    def on_error(self, frame):
        print('received an error "%s"' % frame.body)
    def on_message(self, frame):
        self.message_body = frame.body  # Almacena el cuerpo del mensaje

def doConection():
    activemq_server = "localhost"
    activemq_port = 61613  # Por defecto, ActiveMQ utiliza el puerto 61613 para STOMP
    activemq_username = "admin"
    activemq_password = "admin"
    queue_name = "/queue/queue_handlesensor"
    # Conectar al servidor ActiveMQ
    connection = stomp.Connection([(activemq_server, activemq_port)])
    listener = MyListener(connection)
    connection.set_listener("", listener)
    #connection.start()
    connection.connect(login=activemq_username, passcode=activemq_password, wait=True)
    # Suscribirse a la cola
    connection.subscribe(destination=queue_name, id=1, ack="auto")
    return connection, listener


def logica3(minRange, maxRange):
    print('\n', f'--> Envio de cola aleatorio entre {minRange} y {maxRange} [lat/min]', '\n')
    time.sleep(0.5)
    connection, listener = doConection() #conexion para recibir mensaje desde el interruptor
    queue_name = "/queue/queue_sensor"
    connection_sensor = CONN.conect(queue_name) #conexion para enviar mensajes a la cola del sensor
    flag = True
    on = False
    print('Para salir, pulse la tecla "E"', '\n')
    print('-> Para iniciar envio de mensajes, encienda el sensor con interruptor.', '\n')
    while not keyboard.is_pressed('e'):
        if listener.message_body is not None:
            if listener.message_body == 'on':
                print('Sensor ON', '\n')
                on = True
            elif listener.message_body == 'off':
                print('Sensor OFF', '\n')
                on = False
            listener.message_body = None  # Resetea el cuerpo del mensaje

        if on:
            # Enviar mensaje a la cola
            mensaje = {
            "id_sensor": random.choice(sensores),
            "value": random.randint(minRange, maxRange)
            }
            mensaje_json = json.dumps(mensaje)  # Convertir el objeto Python en una cadena JSON
            connection_sensor.send(body=mensaje_json, destination=queue_name, content_type="application/json")
            print('-> Enviando mensaje')
            time.sleep(1)
    print('Volviendo a menu principal...', '\n')
    time.sleep(1)
    # Desconectar del servidor ActiveMQ
    connection_sensor.disconnect()
    connection.disconnect()