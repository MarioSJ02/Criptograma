# TFG: Cifrado y Descifrado de Archivos con Criptografía Asimétrica

Este proyecto implementa un sistema de **cifrado y descifrado de archivos** usando **criptografía asimétrica** (RSA) con Python. Incluye funcionalidades para la generación y gestión de claves, transmisión segura de claves públicas por red mediante TCP, y almacenamiento persistente de claves en una base de datos.

---

## 📌 Funcionalidades

- 🔐 **Cifrado y descifrado de archivos**
  - Cifrado de archivos con clave pública.
  - Descifrado de archivos con clave privada.

- 🗝️ **Generación de claves asimétricas**
  - Generación de pares de claves RSA (privada y pública).
  - Almacenamiento de claves en formato `.pem`.

- 🌐 **Distribución de claves públicas por red**
  - Envío de la clave pública a través de una conexión TCP.
  - Cliente TCP capaz de recibir y almacenar la clave pública.

- 💾 **Persistencia de claves en base de datos**
  - Guardado de claves en una base de datos SQLite.
  - Recuperación posterior de claves por identificador.

---

## 🛠️ Tecnologías utilizadas

- Python 3
- [`cryptography`](https://cryptography.io/)
- `socket` (TCP/IP)
- `sqlite3`
- `os`, `base64`, `hashlib` (para utilidades adicionales)

---

## 📁 Estructura del proyecto

```text
Criptograma/
│
├── prueba cifrado.txt         # Archivo de prueba para cifrar/descifrar
├── private_key.pem            # Clave privada generada
├── public_key.pem             # Clave pública generada
│
├── dbManager.py               # Módulo para manejar la base de datos de claves
├── keyManager.py              # Generación, carga y gestión de claves RSA
├── fileManager.py             # Funciones para cifrado y descifrado de archivos
├── serverManager.py           # Envío de clave pública mediante TCP
├── layoutManager.py           # Gestión del diseño (si hay interfaz)
├── main.py                    # Script principal del programa
│
├── Script creacion BD/        # Scripts o datos para inicializar la base de datos
├── cliente/                   # Código del cliente que recibe la clave pública
└── __pycache__/               # Archivos compilados automáticamente
``` 
   

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
