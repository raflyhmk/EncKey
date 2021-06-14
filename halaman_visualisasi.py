from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt

def halaman_visualisasi():
    global input_enkripsi, input_dekripsi
    #buat frame
    visualisasi = Toplevel()
    visualisasi.geometry("300x330")
    visualisasi.title("visualisasi")
    #title gui
    title_menu = Label(visualisasi,text="persentase penggunaan", font=("helvetica", 12, "bold", "italic"))
    title_menu.place(x=60, y=10)
    #form input
    label_enkripsi = Label(visualisasi, text="jumlah enkripsi", font=("helvetica", 10))
    label_enkripsi.place(x=30, y=50)
    input_enkripsi = Entry(visualisasi, width=10)
    input_enkripsi.place(x=125, y=55)
    label_dekripsi = Label(visualisasi, text="jumlah dekripsi", font=("helvetica", 10))
    label_dekripsi.place(x=30, y=80)
    input_dekripsi = Entry(visualisasi, width=10)
    input_dekripsi.place(x=125, y=85)
    button_cancel = Button(visualisasi, text="cancel", bg="#351F39", fg="#FAFAFA", command=clear, width=10)
    button_cancel.place(x=30, y=120)
    show_visualisasi = Button(visualisasi, text="visualisasikan", bg="#28527A", fg="#FAFAFA", command=visualisasikan, width=15)
    show_visualisasi.place(x=130, y=120)

def visualisasikan():
    try:
        # Pie chart
        labels = ['enkripsi', 'dekripsi']
        sizes = []
        sizes.insert(0, int(input_enkripsi.get()))
        sizes.insert(1, int(input_dekripsi.get()))
        # only "explode" the 2nd slice (i.e. 'Hogs')
        explode = (0, 0.1)
        #add colors
        colors = ['#ff9999','#66b3ff']
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
        # Equal aspect ratio ensures that pie is drawn as a circle
        ax1.axis('equal')
        plt.title("perbandingan penggunaan")
        plt.tight_layout()
        plt.show()
        
    except ValueError:
        messagebox.showerror('error', "itu bukan angka")  
    

def clear():
    input_enkripsi.delete(0, END)
    input_dekripsi.delete(0, END)
    
