# Criptograma
Desarrollo en Python de un programa de cifrado y descifrado como TFG basado en criptografía asimétrica, implementando algoritmos de clave pública y privada para asegurar la confidencialidad y seguridad de la información

# Instrucciones de instalación

Para ejecutar este proyecto, asegúrate de tener instaladas las siguientes dependencias:
## Linux
1. **Tkinter**  
   Ejecuta el siguiente comando para instalar Tkinter:  
   ```bash
   sudo apt-get install python3-tk
2. **Cryptography**
Instala la librería Cryptography con:
    ```bash
    pip3 install cryptography
3. **MySQL Connector**
  Instala mysql.connector ejecutando el siguiente comando:
   ```bash
     pip3 install mysql-connector-python

## Windows
1. **Tkinter**
   Viene incluido con Python en Windows. Solo asegúrate de tener Python instalado correctamente, verifica con:
   ```bash
   python -m tkinter
3. **Cryptography**
   ```bash
   pip install cryptography
5. **MySQL Connector**
   ```bash
   pip install mysql-connector-python
   
# Parámetros de conexión a la base de datos

      ```python
      config = {
       'user': 'root',
       'password': 'root',
       'host': 'localhost',
       'database': 'keys',
       'port': '3306',
      }
**Nota:** Asegúrate de modificar estos parámetros en el archivo dbmanager.py según tu configuración local 
