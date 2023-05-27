import stomp
import random
import json
import keyboard
import time
import src.conection.conection as CONN
sensores = [1,2,3,4]

def interruptor():
    queue_name = "/queue/queue_handlesensor"
    connection = CONN.conect(queue_name)
    flag = True
    
    print('---- Interruptor de sensor ----')

    while flag:
        print('[1] ON')
        print('[2] OFF')
        print('[otro] Salir de interruptor')
        opcion = input('Ingrese opcion: ')
        print(' ')

        if opcion == '1':
            print('Sensor ON')
            print(' ')
            connection.send(body='on', destination=queue_name, content_type="text/plain")
        elif opcion == '2':
            print('Sensor OFF')
            print(' ')
            connection.send(body='off', destination=queue_name, content_type="text/plain")
        else:
            print('Saliendo de interruptor')
            print(' ')
            flag = False
            
    connection.disconnect()

interruptor()