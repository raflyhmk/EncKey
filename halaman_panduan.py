from tkinter import *

def halaman_panduan():
    panduan = Toplevel()
    panduan.geometry("800x330")
    panduan.title("enkripsi")
    title_panduan = Label(panduan, text="panduan", font=("helvetica", 16, "bold", "italic"))
    title_panduan.place(x=350, y=20)
    buka = open("D:\\enkrip\\panduan.txt")
    baca = buka.read()
    petunjuk_panduan = Label(panduan, text=baca, font=("helvetica", 10))
    petunjuk_panduan.place(x=40, y=50)
    buka.close()
