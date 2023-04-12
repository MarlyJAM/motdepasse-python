import string
from random import randint , choice
from tkinter import *
#

def genarate_password():
    password_min= 6
    password_max= 9
    all_chars= string.ascii_letters + string.punctuation + string.digits
    password = "".join( choice(all_chars) for x in range(randint(password_min,password_max)))
    password_entry.delete(0,END)
    password_entry.insert(0,password)




#creer la fenetre

window = Tk()
window.title("My password python")
window.geometry("720x480")
window.minsize(480,360)
window.config(background='#00c2cb')

#creer la frame principale

first_frame = Frame(window,background='#00c2cb')
#creation d'imgage
width=300
height=300
image = PhotoImage(file='online-security.png').zoom(35).subsample(32)
canvas = Canvas(first_frame,width=width,height=height,background='#00c2cb',bd=0,highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0,column=0,sticky="W")

#creer une sous boite

right_frame = Frame(first_frame,bg='#00c2cb')

# creer le titre
labet_title= Label(right_frame,text="Generer Mon Mot De Passe", font=("Times New Roman",20),bg='#00c2cb')
labet_title.pack()
# creer un champ/entrée/input
password_entry= Entry(right_frame, font=("Times New Roman",20),bg='#ffffff')
password_entry.pack()


# creer un bouton
button =Button(right_frame,text='GENERATE', font=("Times New Roman",10),bg='#00c2cb',command=genarate_password)
button.pack(fill=X)


#afficher la frame
first_frame.pack(expand=YES)
right_frame.grid(row=0,column=1,sticky="W")


#afficher la fenetre

window.mainloop()