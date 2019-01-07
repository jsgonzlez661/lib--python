# -*- coding:utf-8 -*-

# --------------- Modulos importados ---------------
from tkinter.filedialog import askopenfile, asksaveasfilename
from tkinter.messagebox import showinfo
# --------------- Definicion de las clases ---------------

# ----- Clase Padre -----
# Clase necesaria para cargar el documento .log de salida de GAMESS
# Es importante resaltar que el archivo preferiblemente debe estar codificado en utf-8


class documento():

    def __init__(self):  # ----- Constructor de la clase  -----
        self.nombre_doc = ""
        self._archivo = ""
        self.lines = ""  # ----- Se guadara las lineas del documento -----

    def abrir_docexp(self):  # ----- Abrir el archivo .log por el explorador -----
        if(self._archivo == ""):
            opt = ""
            opt = {'defaultextension': '.log',
                   'filetypes': [('Archivo GAMESS', '*.log')]}
            self._archivo = askopenfile(**opt)
        if(self._archivo != None):
            self.lines = reversed(self._archivo.readlines())
            self.lines = list(self.lines)

    def abrir_doc(self):  # ----- Abrir el archivo .log por el nombre -----
        if(self._archivo == ""):
            self.nombre_doc = input(
                "Ingrese el nombre del archivo .log: ") + '.log'
            self._archivo = open(self.nombre_doc, mode='r',
                                 encoding='utf-8', errors='ignore')
            self.lines = reversed(self._archivo.readlines())
            self.lines = list(self.lines)

    def cerrar_doc(self):  # ----- Cerrar el archivo .log -----
        if(self._archivo != "" and self._archivo != None):
            self._archivo.close()

    def _convert_lista(self, lista):  # ----- Convertir las lista de str a float -----
        lista2 = []
        for i in range(0, len(lista)):
            lista2.append(float(str(lista[i])))
        return lista2

    def __del__(self):
        return 0

# ----- Clase para RMN -----
# Clase para buscar los shielding en el archivo de salida
# Es necesario cargar el documento antes de cualquier busqueda


class Shielding(documento):

    def __init__(self):  # ----- Constructor de la clase  -----
        documento.__init__(self)  # ----- Herencia de clase documento -----
        self.valores_13C = []
        self.identificadorC = []
        self.valores_1H = []
        self.identificadorH = []

    def look_shielding(self):  # ----- Buscar Shielding en el documento -----
        if(self._archivo != "" and self.lines != ""):
            i = 0
            salida = ""
            while(salida!="GIAO CHEMICAL SHIELDING TENSOR"):                
                if("C         X" in self.lines[i]):
                    self.identificadorC = self.identificadorC + self.lines[i].split()
                    self.valores_13C = self.valores_13C + self.lines[i-3].split()
                if("H         X" in self.lines[i]):
                    self.identificadorH = self.identificadorH + self.lines[i].split()
                    self.valores_1H = self.valores_1H + self.lines[i-3].split()
                if("GIAO CHEMICAL SHIELDING TENSOR" in self.lines[i]):
                    salida = "GIAO CHEMICAL SHIELDING TENSOR"
                i = i+1
            if(self.valores_13C != []):
                self.valores_13C = self._convert_lista(self.valores_13C)
                self.identificadorC = self.__identificar_atom(
                    self.identificadorC)
            if(self.valores_1H != []):
                self.valores_1H = self._convert_lista(self.valores_1H)
                self.identificadorH = self.__identificar_atom(
                    self.identificadorH)
            else:
                if(self.valores_13C == [] or self.valores_1H == []):
                    return "No existen Shielding en el archivo"

    def __identificar_atom(self, lista):
        if(lista != []):
            atomID = []
            for i in range(0, len(lista)):
                if(lista[i] == 'C'):
                    atomID.append(lista[i-1] + lista[i])
                elif(lista[i] == 'H'):
                    atomID.append(lista[i-1] + lista[i])
            return atomID

    def save_shd(self):  # ----- Guardar en un archivo .txt valores encontrados -----
        if(self.valores_13C != [] and self.valores_1H != []):
            name = ""
            word = {"defaultextension": ".txt", "filetypes": [("Text file", "*.txt")]
                    }
            name = asksaveasfilename(**word)
            if(name != ""):
                doc = open(name, 'w')
                doc.write('Shielding Encontrados\n')
                doc.write('\n')
                doc.write('Carbono Shielding\n')
                for i in range(0, len(self.valores_13C)):
                    doc.write(
                        self.identificadorC[i] + " " + str(self.valores_13C[i]))
                    doc.write('\n')
                doc.write('\n')
                doc.write('Hidrogeno Shielding\n')
                for i in range(0, len(self.valores_1H)):
                    doc.write(
                        self.identificadorH[i] + " " + str(self.valores_1H[i]))
                    doc.write('\n')
                doc.close()
                showinfo("Guardar Archivo", "Archivo Guardado", icon="info")

    def __del__(self):
        return 0
