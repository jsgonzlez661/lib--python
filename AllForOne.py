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
        self._job = ""
        self._lines = ""

    def abrir_docexp(self):  # ----- Abrir el archivo .log por el explorador -----
        if(self._job == ""):
            opt = ""
            opt = {'defaultextension': '.log',
                   'filetypes': [('Archivo GAMESS', '*.log')]}
            self._job = askopenfile(**opt)
        if(self._job != None):
            self._lines = self._job.readlines()

    def abrir_doc(self):  # ----- Abrir el archivo .log por el nombre -----
        if(self._job == ""):
            self.nombre_doc = input(
                "Ingrese el nombre del archivo .log: ") + '.log'
            self._job = open(self.nombre_doc, mode='r',
                             encoding='utf-8', errors='ignore')
            self._lines = self._job.readlines()

    def cerrar_doc(self):  # ----- Cerrar el archivo .log -----
        if(self._job != "" and self._job != None):
            self._job.close()

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
        self.rmn_13C = []
        self.atomid13C = []
        self.rmn_1H = []
        self.atomid1H = []

    def look_shielding(self):  # ----- Buscar Shielding en el documento -----
        if(self._job != "" and self._lines != ""):
            i = 0
            for line in self._lines:
                i = i+1
                if("C         X" in line):
                    self.atomid13C = self.atomid13C + self._lines[i-1].split()
                    self.rmn_13C = self.rmn_13C + self._lines[i+2].split()
                if("H         X" in line):
                    self.atomid1H = self.atomid1H + self._lines[i-1].split()
                    self.rmn_1H = self.rmn_1H + self._lines[i+2].split()
            if(self.rmn_13C != []):
                self.rmn_13C = self._convert_lista(self.rmn_13C)
                self.atomid13C = self.__identificar_atom(self.atomid13C)
            if(self.rmn_1H != []):
                self.rmn_1H = self._convert_lista(self.rmn_1H)
                self.atomid1H = self.__identificar_atom(self.atomid1H)
            else:
                if(self.rmn_13C == [] or self.rmn_1H == []):
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
        if(self.rmn_13C != [] and self.rmn_1H != []):
            name = ""
            word = {"defaultextension": ".txt", "filetypes": [("Text file", "*.txt")]
                    }
            name = asksaveasfilename(**word)
            if(name != ""):
                doc = open(name, 'w')
                doc.write('Shielding Encontrados\n')
                doc.write('\n')
                doc.write('Carbono Shielding\n')
                for i in range(0, len(self.rmn_13C)):
                    doc.write(self.atomid13C[i] + " " + str(self.rmn_13C[i]))
                    doc.write('\n')
                doc.write('\n')
                doc.write('Hidrogeno Shielding\n')
                for i in range(0, len(self.rmn_1H)):
                    doc.write(self.atomid1H[i] + " " + str(self.rmn_1H[i]))
                    doc.write('\n')
                doc.close()
                showinfo("Guardar Archivo", "Archivo Guardado", icon="info")

    def __del__(self):
        return 0
