import stomp

def conect(queue):
    # Configura tus credenciales y dirección del servidor ActiveMQ
    activemq_server = "localhost"
    activemq_port = 61613  # Por defecto, ActiveMQ utiliza el puerto 61613 para STOMP
    activemq_username = "admin"
    activemq_password = "admin"
    queue_name = queue

    # Conectar al servidor ActiveMQ
    connection = stomp.Connection([(activemq_server, activemq_port)])
    #connection.set_listener("", stomp.PrintingListener())
    #connection.start()
    connection.connect(login=activemq_username, passcode=activemq_password, wait=True)
    
    return connection
