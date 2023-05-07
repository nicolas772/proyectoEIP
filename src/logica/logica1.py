import stomp
import random
import json
import keyboard
import time
import src.conection.conection as CONN
sensores = [1,2,3,4]

def logica1(minRange, maxRange):
    print('\n', f'--> Envio de cola aleatorio entre {minRange} y {maxRange} [lat/min]', '\n')
    time.sleep(0.5)
    queue_name = "/queue/queue_sensor"
    connection = CONN.conect(queue_name)
    print('Para dejar de enviar mensajes, pulse la tecla "E"', '\n')
    
    while not keyboard.is_pressed('e'):
        # Enviar mensaje a la cola
        mensaje = {
        "id_sensor": random.choice(sensores),
        "value": random.randint(minRange, maxRange)
        }
        mensaje_json = json.dumps(mensaje)  # Convertir el objeto Python en una cadena JSON
        connection.send(body=mensaje_json, destination=queue_name, content_type="application/json")
        time.sleep(1)

    # Desconectar del servidor ActiveMQ
    connection.disconnect()