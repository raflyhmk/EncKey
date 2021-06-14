from tkinter import *
from fungsi_enkripsi import enkrip, halaman_enkripsi
from fungsi_dekripsi import dekrip, halaman_dekripsi
from halaman_panduan import halaman_panduan
from halaman_visualisasi import halaman_visualisasi, visualisasikan


mainframe = Tk()
mainframe.title('EncKey')
mainframe.geometry("400x300")

toolbar = Menu(mainframe)  
mainframe.config(menu=toolbar)

opsi_menu = Menu(toolbar)  
toolbar.add_cascade(label='help', menu=opsi_menu)  
opsi_menu.add_command(label='panduan', command=halaman_panduan)
opsi_menu.add_command(label='visualisasi', command=halaman_visualisasi)

judul = Label(mainframe, text="EncKey", font=("helvetica", 16, "italic"))
judul.place(x=150, y=20)

slogan = Label(mainframe, text="ubah pesan menjadi sesuatu yang kamu ketahui", font=("helvetica", 12))
slogan.place(x=30, y=50)

menu_enkrip = Button(mainframe, text="enkripsi", bg="#28527A", fg="#FAFAFA", command=halaman_enkripsi, width=10)
menu_enkrip.place(x=30, y=100)

menu_dekrip = Button(mainframe, text="dekripsi", bg="#351F39", fg="#FAFAFA", command=halaman_dekripsi, width=10)
menu_dekrip.place(x=230, y=100)


mainframe.mainloop()

