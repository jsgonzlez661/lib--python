

archivo = open("prueba.log", 'r')

lineas = archivo.readlines()
listaC = []
listanumC = []
i=0
inver = reversed(lineas)
estado = list(inver)
for line in estado:
    
    #s = "C         X"
    #print(line.index(s))  
    if("C         X" in line):
        listaC = listaC + line.strip('\n').split()
        listanumC = listanumC + estado[i-3].split()
    if("GIAO CHEMICAL SHIELDING TENSOR" in line):
        print("cerrado")
        break    
    i = i + 1 
    
print(listanumC)
print(listaC)


archivo.close()