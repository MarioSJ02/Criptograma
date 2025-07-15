from cryptography.hazmat.primitives.asymmetric import  padding
from cryptography.hazmat.primitives import serialization, hashes


class FileManager:

    def encryptFile(self,filePath,publicKeyPath):
        try:
            # Lee el archivo de entrada
            with open(filePath, 'rb') as f:
                plaintext = f.read()
        
            # Carga la clave pública
            with open(publicKeyPath, 'rb') as f:
                self.publicKey = serialization.load_pem_public_key(f.read())

            # Cifra el contenido del archivo
            ciphertext = self.publicKey.encrypt(
                plaintext,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )

            # Escribe el archivo cifrado
            with open(filePath, 'wb') as f:
                f.write(ciphertext)
            return True  
        except Exception:
            return False
            
    def decryptFile(self,filePath,privateKeyPath):
        try:
            # Lee el archivo cifrado
            with open(filePath, 'rb') as f:
                ciphertext = f.read()

            # Carga la clave privada
            with open(privateKeyPath, 'rb') as f:
                privateKey = serialization.load_pem_private_key(f.read(), password=None)

            # Descifra el contenido del archivo
            plaintext = privateKey.decrypt(
                ciphertext,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )

            # Escribe el archivo descifrado
            with open(filePath, 'wb') as f:
                f.write(plaintext)
            return True
            messagebox.showinfo("Éxito", "El archivo ha sido descifrado exitosamente.")
        except Exception as e:
            return False
            messagebox.showerror("Error", f"Ocurrió un error al descifrar el archivo: {str(e)}")

