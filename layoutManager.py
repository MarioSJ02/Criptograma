import tkinter as tk
from tkinter import filedialog, messagebox

class LayoutManager:
    def __init__(self, master):
        self.master = master
        master.title("Cifrado y descifrado de archivos")
        # CENTRAR LA VENTANA PRINCIPAL
        # Obtener las dimensiones de la pantalla
        screenWidth = master.winfo_screenwidth()
        screenHeight = master.winfo_screenheight()

        self.filePath = tk.StringVar()
        self.privateKeyPath = tk.StringVar()
        self.publicKeyPath = tk.StringVar()

        # Centrar la ventana principal
        x = (screenWidth - master.winfo_reqwidth()) / 2
        y = (screenHeight - master.winfo_reqheight()) / 2
        master.geometry("+%d+%d" % (x, y))

        tk.Label(master, text="Elige el archivo para cifrarlo:").grid(row=0, column=0, padx=8, pady=7)
        tk.Entry(master, textvariable=self.filePath, width=30,state="readonly").grid(row=0, column=1, padx=8, pady=7)
        self.selectFileBtn = tk.Button(master, text="Seleccionar archivo")
        self.selectFileBtn.grid(row=0, column=2, padx=8, pady=7)

        tk.Label(master, text="Clave privada:").grid(row=1, column=0, padx=8, pady=7)
        tk.Entry(master, textvariable=self.privateKeyPath, width=30,state="readonly").grid(row=1, column=1, padx=8, pady=7)
        self.selectPrivateKey = tk.Button(master, text="Seleccionar archivo")
        self.selectPrivateKey.grid(row=1, column=2, padx=8, pady=7)

        tk.Label(master, text="Clave pública:").grid(row=2, column=0, padx=8, pady=7)
        tk.Entry(master, textvariable=self.publicKeyPath, width=30,state="readonly").grid(row=2, column=1, padx=8, pady=7)
        self.selectPublicKey = tk.Button(master, text="Seleccionar archivo")
        self.selectPublicKey.grid(row=2, column=2, padx=8, pady=7)

        self.encryptFileBtn = tk.Button(master, text="Cifrar archivo")
        self.encryptFileBtn.grid(row=3, column=0, padx=8, pady=7)
        self.decryptFileBtn = tk.Button(master, text="Descifrar archivo")
        self.decryptFileBtn.grid(row=3, column=1, padx=8, pady=7)
        self.generateKeysBtn = tk.Button(master, text="Generar claves")
        self.generateKeysBtn.grid(row=3, column=2, padx=8, pady=7)
        self.findKeysBtn = tk.Button(master, text="Buscar claves en la base de datos")
        self.findKeysBtn.grid(row=4, column=1, columnspan=2, padx=8, pady=7)

        self.sendKeyBtn = tk.Button(master, text="Distribuir clave pública")
        self.sendKeyBtn.grid(row=4, column=0, padx=8, pady=7)



    # Getters de los botones 
    def getSelectFileBtn(self):
        return self.selectFileBtn

    def getSelectPrivateKey(self):
        return self.selectPrivateKey

    def getSelectPublicKey(self):
        return self.selectPublicKey
    
    def getEncryptFileBtn(self):
        return self.encryptFileBtn
    
    def getDecryptFileBtn(self):
        return self.decryptFileBtn
    
    def getGenerateKeysBtn(self):
        return self.generateKeysBtn
    
    def getfindKeysBtn(self):
        return self.findKeysBtn
    
    def getSendKeyBtn(self):
        return self.sendKeyBtn
        

    #Setters de los Entrys
    def setFilePath(self,filePath):
        self.filePath.set(filePath)

    def setPublicKeyPath(self,filePath):
        self.publicKeyPath.set(filePath)

    def setPrivateKeyPath(self,filePath):
        self.privateKeyPath.set(filePath)

    
    #Para la busqueda en la base de datos
    def showInputWindow(self):
        self.inputWindow = tk.Toplevel(self.master)
        self.inputWindow.title("Introducir id")
        # Obtener las dimensiones de la pantalla
        screenWidth = self.inputWindow.winfo_screenwidth()
        screenHeight = self.inputWindow.winfo_screenheight()

        # Centrar la ventana secundaria
        x = (screenWidth - self.inputWindow.winfo_reqwidth()) / 2
        y = (screenHeight - self.inputWindow.winfo_reqheight()) / 2
        self.inputWindow.geometry("+%d+%d" % (x, y))

        self.inputWindow.geometry("200x100")

        tk.Label(self.inputWindow, text="Introducir id:").pack()
        # Insertar el valor "1", por defecto, en la entrada de texto
        self.id = tk.IntVar(value=1)
        tk.Entry(self.inputWindow, textvariable=self.id).pack()

        return tk.Button(self.inputWindow, text="Buscar en la BD")


    #Confirma que la id sea valida
    def validateInput(self):
        try:
            id_value = int(self.id.get())
            if id_value < 0:
                raise ValueError()
        except ValueError:
            return -1
        else:
            self.inputWindow.destroy()    
            return id_value

    def selectFile(self,filetypes):
        filePath = filedialog.askopenfilename(filetypes=filetypes)
        if filePath:
            return filePath


    def showSendData(self):
        self.sendDataWindow = tk.Toplevel(self.master)
        self.sendDataWindow.title("PRUEBA")
        # Obtener las dimensiones de la pantalla
        screenWidth = self.sendDataWindow.winfo_screenwidth()
        screenHeight = self.sendDataWindow.winfo_screenheight()

        # Centrar la ventana secundaria
        x = (screenWidth - self.sendDataWindow.winfo_reqwidth()) / 2
        y = (screenHeight - self.sendDataWindow.winfo_reqheight()) / 2
        self.sendDataWindow.geometry("+%d+%d" % (x, y))

        self.sendDataWindow.geometry("200x200")

        tk.Label(self.sendDataWindow, text="Enviando informacion a clientes").pack()
        
        return tk.Button(self.sendDataWindow, text="Detener envio")
    
    def closeSendData(self):
        self.sendDataWindow.destroy()



    # Mostrar informacion para el usuario
    def showInfo(self,message):
        messagebox.showinfo(message[0], message[1])

    # Mostrar errores para el usuario
    def showError(self,error):
        messagebox.showerror(error[0],error[1])
    
    # Mostrar alertas para el usuario
    def showWarning(self,warning):
        messagebox.showwarning(warning[0],warning[1])
