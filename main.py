import tkinter as tk

from layoutManager import LayoutManager
from layoutManager import LayoutManager
from layoutManager import LayoutManager
from keyManager import KeyManager
from fileManager import FileManager
from serverManager import ServerManager


class Main:
    def __init__(self):
        # Iniciar GUI
        root = tk.Tk()
        self.layout = LayoutManager(root)

        # Inicializar los administradores 
        self.fileManager = FileManager()
        self.keyManager = KeyManager()
        self.serverManager = ServerManager()


        #Paths de los archivos
        self.filePath = ""
        self.privateKeyPath = ""
        self.publicKeyPath = ""


        # Obtenemos todos los botones
        self.selectFileBtn = self.layout.getSelectFileBtn()
        self.selectPrivateKeyBtn = self.layout.getSelectPrivateKey()
        self.selectPublicKeyBtn = self.layout.getSelectPublicKey()
        self.generateKeysBtn = self.layout.getGenerateKeysBtn()
        self.findKeysBtn = self.layout.getfindKeysBtn()
        self.encryptFileBtn = self.layout.getEncryptFileBtn()
        self.decryptFileBtn = self.layout.getDecryptFileBtn()

        self.sendKeyBtn = self.layout.getSendKeyBtn()
        

        #Asignamos las funciones de los botones
        self.selectFileBtn.config(command=self.selectFile)
        self.selectPrivateKeyBtn.config(command=self.selectPrivateKey)
        self.selectPublicKeyBtn.config(command=self.selectPublicKey)
        self.generateKeysBtn.config(command=self.generateKeys)
        self.findKeysBtn.config(command=self.findKeys)
        self.encryptFileBtn.config(command=self.encryptFile)
        self.decryptFileBtn.config(command=self.decryptFile)
        self.sendKeyBtn.config(command=self.sendKey)


        root.mainloop()

    # Selecciona un archivo de texto y guarda su ruta
    def selectFile(self):   
        filetypes = [("Archivos de texto", "*.txt")]
        self.filePath = self.layout.selectFile(filetypes)
        self.layout.setFilePath(self.filePath)

    # Selecciona un archivo de claves públicas y guarda su ruta
    def selectPublicKey(self):
        filetypes=[("Archivos de claves", "*.pem")]
        self.publicKeyPath = self.layout.selectFile(filetypes)
        self.layout.setPublicKeyPath(self.publicKeyPath)
    
    # Selecciona un archivo de claves privadas y guarda su ruta
    def selectPrivateKey(self):
        filetypes=[("Archivos de claves", "*.pem")]
        self.privateKeyPath = self.layout.selectFile(filetypes)
        self.layout.setPrivateKeyPath(self.privateKeyPath)

    
    # Generar claves y guardar las rutas
    def generateKeys(self):
        self.privateKeyPath = "private_key.pem"
        self.layout.setPrivateKeyPath(self.privateKeyPath)

        self.publicKeyPath = "public_key.pem"
        self.layout.setPublicKeyPath(self.publicKeyPath)

        if(self.keyManager.generateKey()):
            message=["Éxito", "Se han generado las claves exitosamente"]
            self.layout.showInfo(message)
        else:
            error=["Error", "No se han generado correctamente las claves"]
            self.layout.showError(error)
    #Busqueda de claves en la BD
    def findKeys(self):
        self.findIdBtn  = self.layout.showInputWindow()
        self.findIdBtn.config(command=self.validateInput)
        self.findIdBtn.pack()


    def validateInput(self):
        id = self.layout.validateInput()
        if id == -1:
            error=["Error", "El numero debe ser mayor de 0"]
            self.layout.showError(error)
        else:
            if self.keyManager.getKeysFromDB(id):
                self.privateKeyPath = "private_key.pem"
                self.layout.setPrivateKeyPath(self.privateKeyPath)

                self.publicKeyPath = "public_key.pem"
                self.layout.setPublicKeyPath(self.publicKeyPath)

                message=["Éxito", "Claves recibidas correctamente"]
                self.layout.showInfo(message)

            else:
                error=["Error", "No existen las claves con la id proporcionada"]
                self.layout.showError(error)

    def encryptFile(self):
        # Validamos que haya un archivo seleccionado
        if self.filePath == "":
            warning = ["Aviso", "Primero debes seleccionar un archivo a cifrar"]
            self.layout.showWarning(warning)
        else:
            # Validamos que haya una clave publica seleccionada
            if self.publicKeyPath == "":
                warning = ["Aviso", "Primero debes seleccionar una clave publica para cifrar"]
                self.layout.showWarning(warning)
            else:
                if self.fileManager.encryptFile(self.filePath,self.publicKeyPath):
                    message = ["Éxito", "El archivo ha sido cifrado exitosamente."]
                    self.layout.showInfo(message)
                else:
                    error = ["Error", "Ocurrió un error al cifrar el archivo"]
                    self.layout.showError(error)
        
            

    def decryptFile(self):
        # Validamos que haya un archivo seleccionado
        if self.filePath == "":
            warning = ["Aviso", "Primero debes seleccionar un archivo a cifrar"]
            self.layout.showWarning(warning)
        else:
            # Validamos que haya una clave privada seleccionada
            if self.privateKeyPath == "":
                warning = ["Aviso", "Primero debes seleccionar una clave privada para cifrar"]
                self.layout.showWarning(warning)
            else:
                if self.fileManager.decryptFile(self.filePath,self.privateKeyPath):
                    message = ["Éxito", "El archivo ha sido descifrado exitosamente."]
                    self.layout.showInfo(message)
                else:
                    error = ["Error", "Ocurrió un error al descifrar el archivo"]
                    self.layout.showError(error)


    def sendKey(self):
            if self.publicKeyPath == "":
                error = ["Error", "Primero debes seleccionar una clave pública para enviarla"]
                self.layout.showError(error)
            else:
                self.stopServerBtn = self.layout.showSendData()
                self.stopServerBtn.config(command=self.stopServer) 
                self.stopServerBtn.pack()
                self.serverManager.start(self.publicKeyPath)

    def stopServer(self):
        self.serverManager.stopServer()
        self.layout.closeSendData()
#Arrancamos la aplicacion
if __name__ == '__main__':
    Main()
