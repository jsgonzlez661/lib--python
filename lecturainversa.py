

archivo = open("prueba.log", 'r')

line = list(reversed(archivo.readline().strip()))
cnt = 1

while line:
    print(line)
    line = list(reversed(archivo.readline().strip()))
    cnt += 1

archivo.close()