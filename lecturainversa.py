

archivo = open("prueba.log", 'r')

line = list(reversed(archivo.readlines()))
#print(line)

identificador = []
valores = []
hasta = ""
i=0
while hasta!="GIAO CHEMICAL SHIELDING TENSOR":
    if("C         X" in line[i]):
        identificador = identificador + line[i].split()        
        valores = valores + line[i-3].split()
    if("GIAO CHEMICAL SHIELDING TENSOR" in line[i]):
        hasta = "GIAO CHEMICAL SHIELDING TENSOR"
    i += 1

print(identificador)
print(valores)
archivo.close()