import stomp
import random
import json
import keyboard
import time
import src.conection.conection as CONN
sensores = [1,2,3,4]

def isInRange(min, max, mensaje):
    return (min < mensaje['value'] < max)

def createAlternateMessage(min, max, turn):
    if turn:
       mensaje = {
        "id_sensor": random.choice(sensores),
        "value": random.randint(min, max)
        }
    else:
        mensaje = {
        "id_sensor": random.choice(sensores),
        "value": random.randint(max + 1, 1000000000)
        }
    return mensaje

def manageSend(min, max, mensaje, connection, queue_name):
    if isInRange(min, max, mensaje):
        mensaje_json = json.dumps(mensaje)  # Convertir el objeto Python en una cadena JSON
        connection.send(body=mensaje_json, destination=queue_name, content_type="application/json")
        print('\n',"--> Mensaje JSON enviado a la cola.")
        print(f"--> min: {min} max: {max} valor: {mensaje['value']}.")

    else:
        print('\n',"--> El mensaje no puede ser enviado.")
        print(f"--> min: {min} max: {max} valor: {mensaje['value']}.",'\n')

def logica2(minRange, maxRange):
    print('\n', f'--> Envio de cola aleatorio entre {minRange} y {maxRange} [lat/min]', '\n')
    time.sleep(0.5)
    queue_name = "/queue/queue_sensor"
    connection = CONN.conect(queue_name)
    print('Para dejar de enviar mensajes, pulse la tecla "E"', '\n')
    turn = True
    while not keyboard.is_pressed('e'):
        # Enviar mensaje a la cola
        if turn:
            mensaje = createAlternateMessage(minRange, maxRange, turn)
            turn = False
        else:
            mensaje = createAlternateMessage(minRange, maxRange, turn)
            turn = True
        
        manageSend(minRange, maxRange, mensaje, connection, queue_name)
        time.sleep(1)

    # Desconectar del servidor ActiveMQ
    connection.disconnect()