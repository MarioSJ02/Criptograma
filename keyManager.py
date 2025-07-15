from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from dbManager import DbManager

class KeyManager:
    def __init__(self):
        self.dbManager = DbManager()
        self.publicKey = None
        self.privateKey = None
        
    def generateKey(self):
        # Genera una clave privada RSA de 2048 bits
        self.privateKey = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )

        # Obtiene la clave pública correspondiente a partir de la privada
        self.publicKey = self.privateKey.public_key()

        with open("private_key.pem" , 'wb') as f:
            f.write(self.privateKey.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            ))
        with open("public_key.pem", 'wb') as f:
            f.write(self.publicKey.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ))        
        
        if(self.dbManager.insertKeys(self.publicKey,self.privateKey)):
            self.dbManager.disconnect()
            return True
        else:
            self.dbManager.disconnect()
            return False
    

    def getKeysFromDB(self,id):
        result = self.dbManager.getKeysFromDB(id)
        if result is None:
            self.dbManager.disconnect()
            return False
        else:
            private_key_text = result[0]
            public_key_text = result[1]
        # Crear objetos RSA a partir de las claves en formato texto
        self.privateKey = serialization.load_pem_private_key(private_key_text.encode(), password=None)
        self.publicKey = serialization.load_pem_public_key(public_key_text.encode())


        
        with open("private_key.pem", "wb") as f:
            f.write(self.privateKey.private_bytes(encoding=serialization.Encoding.PEM,
                                            format=serialization.PrivateFormat.PKCS8,
                                            encryption_algorithm=serialization.NoEncryption()))

        with open("public_key.pem", "wb") as f:
            f.write(self.publicKey.public_bytes(encoding=serialization.Encoding.PEM,
                                            format=serialization.PublicFormat.SubjectPublicKeyInfo))
        self.dbManager.disconnect()
        return True



