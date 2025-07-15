import mysql.connector
from cryptography.hazmat.primitives import serialization


class DbManager:
    def __init__(self):
        # Conectamos con la bd
        self.connect()
        # Crear la tabla 'keys' si no existe
        self.createTable()

    def createTable(self):
        mycursor = self.mydb.cursor()
        mycursor.execute('''CREATE TABLE IF NOT EXISTS `keys` (
                            id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
                            private_key TEXT,
                            public_key TEXT
                        )''')
        mycursor.close()
    # Insertamos en la base de datos las claves
    def insertKeys(self, publicKey, privateKey):
        # Crea la conexion con la base de datos
        self.connect()
        try:
            mycursor = self.mydb.cursor()

            privateKeyBytes = privateKey.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            )
            publicKeyBytes = publicKey.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )

            mycursor.execute("INSERT INTO `keys` (private_key, public_key) VALUES (%s, %s)",
                            (privateKeyBytes, publicKeyBytes))

            self.mydb.commit()
            mycursor.close()
            return True
        except Exception as e:
            print(f"Error al insertar las claves en la base de datos: {str(e)}")
            return False
        
    def getKeysFromDB(self,id):
        # Crea la conexion con la base de datos
        self.connect()
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT private_key, public_key FROM `keys` WHERE id = %s", (id,))
        result = mycursor.fetchone()

        if result is not None:
            return result
        else:
            return None



    # Conectarse a la base de datos
    def connect(self):
        # Parámetros de conexión a la base de datos
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'localhost',
            'database': 'keys',
            'port': '3306', 
        }
        # Crear la conexión a la base de datos
        self.mydb = mysql.connector.connect(**config)

    # Desconectarse de la base de datos
    def disconnect(self):
        # Cerrar la conexión a la base de datos
        self.mydb.close()
