from tkinter import *
from tkinter import messagebox
import re

abjad = ['a','b','c','d','e','f','g','h',
         'i','j','k','l','m','n','o','p',
         'q','r','s','t','u','v','w','x',
         'y','z']

def halaman_enkripsi():
    global form_input, hasil_kalimat, button_enkrip
    #buat frame
    enkripsi = Toplevel()
    enkripsi.geometry("800x330")
    enkripsi.title("enkripsi")
    #title gui
    title_menu = Label(enkripsi,text="Enkripsi", font=("helvetica", 16, "bold", "italic"))
    title_menu.place(x=330, y=20)
    #form input
    label_enkripsi = Label(enkripsi,text="masukan kata:", font=("helvetica", 12))
    label_enkripsi.place(x=30, y=60)
    form_input = Text(enkripsi, width=40, height=10)
    form_input.place(x=30, y=90)
    #hasil output
    hasil_title = Label(enkripsi, text="kata yang dihasilkan", font=("helvetica", 12))
    hasil_title.place(x=400, y=60)
    hasil_kalimat = Text(enkripsi, width=40, height=10)
    hasil_kalimat.place(x=400, y=90)
    #button back & submit enkripsi
    button_cancel = Button(enkripsi, text="cancel", bg="#351F39", fg="#FAFAFA", command=clear, width=10)
    button_cancel.place(x=30, y=270)
    button_enkrip = Button(enkripsi, text="enkripsi", bg="#28527A", fg="#FAFAFA", command=submit_enkripsi, width=10)
    button_enkrip.place(x=230, y=270)

def enkrip(form_input):
  hasil_enkrip=''
  kalimat_check= re.compile('[@_!#$%^&*()<>?/\|}{~:0-9A-Z]')
  try:    
      if len(form_input) > 400:
          raise(NameError)
      else:
          for karakter in form_input:
              if(kalimat_check.search(form_input) != None):
                  raise(ValueError)
              else:
                  if karakter in abjad:
                      index_lama = abjad.index(karakter)
                      index_enkrip = (index_lama + 5 ) % len(abjad)
                      abjad_enkrip = abjad[index_enkrip]
                      hasil_enkrip += abjad_enkrip
                  else:
                      hasil_enkrip += ' '   
  except(ValueError):
    messagebox.showwarning('warning', "hanya menerima input berupa huruf kecil")
  except(NameError):
    messagebox.showerror('error', "jumlah karakter input melebihi 400 karakter")  
  return hasil_enkrip

def clear():
    button_enkrip.config(state=NORMAL)
    form_input.delete(1.0, END)
    hasil_kalimat.delete(1.0, END)
def submit_enkripsi():
    button_enkrip.config(state=DISABLED)
    hasil_enkripsi = enkrip(form_input.get(1.0, END))
    hasil_kalimat.insert(END, hasil_enkripsi)






