import socket

def receiveData(server_address):
    # Creamos el socket del cliente
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Conectamos al servidor
        client_socket.connect(server_address)

        # Recibimos los datos del archivo
        data = b""
        while True:
            chunk = client_socket.recv(1024)
            if not chunk:
                break
            data += chunk

        # Guardamos los datos en un archivo
        with open("clave.pem", "wb") as file:
            file.write(data)

        print("Archivo recibido y guardado correctamente.")

    except ConnectionRefusedError:
        print("No se pudo establecer la conexión con el servidor.")
    except Exception as e:
        print(f"Error al recibir y guardar el archivo: {str(e)}")

    # Cerramos el socket del cliente
    client_socket.close()

# Dirección y puerto del servidor
server_address = ('localhost', 8888)

# Llamamos a la función para recibir los datos del servidor
receiveData(server_address)
