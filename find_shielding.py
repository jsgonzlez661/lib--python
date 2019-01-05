# -*- coding:utf-8 -*-
import tkinter as tk
import tkinter.filedialog as fd
from AllForOne import Shielding

raiz = tk.Tk()
raiz.geometry("400x250")
raiz.title("FIND SHIELDING TENSOR (PPM)")
raiz.resizable(0, 0)
# raiz.iconbitmap("find.ico")

miFrame = tk.Frame()
miFrame.pack()


wellcome = tk.Label(
    miFrame, text="WELLCOME\n\n find SHIELDING in files GAMESS", font="50")
wellcome.grid(row=0, column=0, columnspan=3)
wellcome.config(height=5)
shdScreen = tk.StringVar()

rmn = ""
job = ""


def open_log():
    global escudo
    escudo = Shielding()
    escudo.abrir_docexp()


def find_rmn():  # Buscar los valores de SHIELDING en el archivo .log
    global rmn
    escudo.look_shielding()
    if(escudo.rmn_13C != [] and escudo.rmn_1H != []):
        rmn = escudo.rmn_13C + escudo.rmn_1H
    if(rmn != ""):
        shdScreen.set(rmn)
    escudo.cerrar_doc()


def save_rmn():  # Crear y save los valores encontrados
    escudo.save_shd()
    # print("listo")


open_p = tk.Button(miFrame, text="Open GAMESS output file",
                   command=lambda: open_log())
open_p.grid(row=1, column=0, padx=10, pady=10)

search_p = tk.Button(miFrame, text="Find SHIELDING",
                     command=lambda: find_rmn())
search_p.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

text_title = tk.Label(miFrame, text="SHIELDING found:")
text_title.grid(row=2, column=0)

shd = tk.Entry(miFrame, textvariable=shdScreen)
shd.grid(row=3, column=0, columnspan=3, padx=10)  # , pady=10)
shd.config(width=50)


save = tk.Button(miFrame, text="Save", command=lambda: save_rmn())
save.grid(row=4, column=0, columnspan=1, padx=20, pady=20,)
save.config(width=10)

exit = tk.Button(miFrame, text="Exit", command=lambda: miFrame.quit())
exit.grid(row=4, column=2, columnspan=1, padx=20, pady=20)
exit.config(width=10)

raiz.mainloop()
