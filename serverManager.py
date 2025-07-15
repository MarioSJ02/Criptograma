import socket
import threading

class ServerManager:
    def __init__(self):
        self.connections = {}  # Diccionario para almacenar las conexiones y direcciones de los clientes
        self.serverSocket = None  # Variable para almacenar el socket del servidor
        self.serverThread = None  # Variable para almacenar el hilo del servidor

    def start(self, publicKeyPath):
        # Creamos el socket del servidor
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Definimos la dirección y puerto del servidor
        server_address = ('localhost', 8888)
        self.serverSocket.bind(server_address)

        # Llamamos al método listen() para que el socket del servidor esté listo para aceptar conexiones
        self.serverSocket.listen()

        # Creamos un hilo para el servidor y lo iniciamos
        self.serverThread = threading.Thread(target=self.runServer, args=(publicKeyPath,))
        self.serverThread.start()

    def runServer(self, publicKeyPath):
        while True:
            # Aceptamos la conexión del cliente
            client_socket, client_address = self.serverSocket.accept()

            # Guardamos la información en el diccionario
            self.connections[client_address] = client_socket

            # Enviamos los datos al cliente recién conectado
            self.sendData(client_socket, publicKeyPath)

    def sendData(self, client_socket, publicKeyPath):
        # Abrimos el archivo .pem y lo leemos
        with open(publicKeyPath, 'rb') as file:
            data = file.read()

        # Enviamos los datos del archivo al cliente
        client_socket.sendall(data)

        # Cerramos la conexión con el cliente
        client_socket.close()

    def stopServer(self):
        # Detener el servidor cerrando todas las conexiones
        for client_socket in self.connections.values():
            client_socket.close()

        self.connections.clear()  # Limpiar el diccionario de conexiones

        # Cerramos el socket del servidor
        if self.serverSocket:
            self.serverSocket.close()

        # Esperamos a que el hilo del servidor termine
        if self.serverThread:
            self.serverThread.join()
