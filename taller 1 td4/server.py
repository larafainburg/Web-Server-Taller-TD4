from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)

# Preparar el socket del server
serverSocket.bind(('', 6789))
serverSocket.listen(1)

while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()  # Aceptar la conexión
    try:
        message = connectionSocket.recv(1024).decode()  # Recibir el mensaje
        filename = message.split()[1]  # Resolver qué recurso pide el mensaje
        f = open(filename[1:], 'rb')
        data_respuesta = f.read()  # Cargar el recurso

        # Enviar el header HTTP de la respuesta
        header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n'
        connectionSocket.send(header.encode())

        # La siguiente línea envía el contenido de la respuesta
        connectionSocket.send(data_respuesta)
        connectionSocket.close()

    except IOError:
        # En caso de no tener el archivo, enviar mensaje HTTP correspondiente
        error = 'HTTP/1.1 404 Not Found\r\n\r\n<h1>404 Not Found</h1>'
        connectionSocket.send(error.encode())
        connectionSocket.close()
        sys.exit()  # Terminate the program after sending the corresponding data

serverSocket.close()