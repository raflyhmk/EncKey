from tkinter import *
import re

abjad = ['a','b','c','d','e','f','g','h',
         'i','j','k','l','m','n','o','p',
         'q','r','s','t','u','v','w','x',
         'y','z']

def halaman_dekripsi():
    global form_input, hasil_kalimat, button_dekrip
    #buat frame
    dekripsi = Toplevel()
    dekripsi.geometry("800x330")
    dekripsi.title("dekripsi")
    #title gui
    title_menu = Label(dekripsi,text="Dekripsi", font=("helvetica", 16, "bold", "italic"))
    title_menu.place(x=330, y=20)
    #form input
    label_dekripsi = Label(dekripsi,text="masukan kata:", font=("helvetica", 12))
    label_dekripsi.place(x=30, y=60)
    form_input = Text(dekripsi, width=40, height=10)
    form_input.place(x=30, y=90)
    #hasil output
    hasil_title = Label(dekripsi, text="kata yang dihasilkan", font=("helvetica", 10))
    hasil_title.place(x=400, y=60)
    hasil_kalimat = Text(dekripsi, width=40, height=10)
    hasil_kalimat.place(x=400, y=90)
    #button back & submit dekripsi
    button_cancel = Button(dekripsi, text="cancel", bg="#351F39", fg="#FAFAFA", command=clear, width=10)
    button_cancel.place(x=30, y=270)
    button_dekrip = Button(dekripsi, text="dekripsi", bg="#28527A", fg="#FAFAFA", command=submit_dekripsi, width=10)
    button_dekrip.place(x=230, y=270)

def dekrip(form_input):
  hasil_dekrip=''
  kalimat_check= re.compile('[@_!#$%^&*()<>?/\|}{~:0-9A-Z]')  
  for karakter in form_input:
    if(kalimat_check.search(form_input) == None): 
      if karakter in abjad:
        index_lama = abjad.index(karakter)
        index_dekrip = (index_lama - 5 ) % len(abjad)
        abjad_dekrip = abjad[index_dekrip]
        hasil_dekrip += abjad_dekrip
      else:
         hasil_dekrip += ' '
    else:
      hasil_dekrip = "input tidak boleh huruf kapital/simbol/angka"
  return hasil_dekrip

def clear():
    button_dekrip.config(state=NORMAL)
    form_input.delete(1.0, END)
    hasil_kalimat.delete(1.0, END)
def submit_dekripsi():
    button_dekrip.config(state=DISABLED)
    hasil_dekiripsi = dekrip(form_input.get(1.0, END))
    hasil_kalimat.insert(END, hasil_dekiripsi)







