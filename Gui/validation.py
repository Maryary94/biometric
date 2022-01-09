import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
import os
from tkinter.constants import N, SUNKEN, S
from PIL import Image, ImageTk



validation1 =tk.Tk()
#-------------estrutura da aplicação, color e icon------------------
validation1.title("Bio application")
validation1.geometry('1280x720')
validation1.config(bg='#263d42') 
validation1.iconbitmap("Images/fingerprint2.ico")
#-------------------------------------------------------------------


#----------------------------logotipo-------------------------------
logo = Image.open('Images/biom.png')
logo= logo.resize((150, 200), Image.ANTIALIAS )
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
#-------------------------------------------------------------------

# # Informação
instructions = tk.Label(validation1,text="Insert your fingerprint on the device",font=("Arial", 25))




def val2():
    delete_all()
    validation2.grid(row=0, column=0, padx=35, pady=30)
    
    info_frame = LabelFrame(validation2, padx=470, pady=50 )
    forInfo_Frame = Label(info_frame, text="Adicionar Instruções",padx=15, pady=15,font=("Arial", 18))
    
    frame = LabelFrame(validation2, padx=50, pady=50 )
    
    
    # Para se mudar para o video
    testeImageToChangeToVideo= Image.open('Images/bio-info.png')
    testeImageToChangeToVideo= testeImageToChangeToVideo.resize((350, 300), Image.ANTIALIAS )
    testeImageToChangeToVideo = ImageTk.PhotoImage(testeImageToChangeToVideo)
    img_label = tk.Label(image=testeImageToChangeToVideo)
    img_label.image = testeImageToChangeToVideo
    forFrameTeste = Label(frame, image=testeImageToChangeToVideo)
    
    # forFrame = Label(frame, text="frame!",padx=5, pady=15)
    
    
    
    
    
    
    frame1 = LabelFrame(validation2, padx=50, pady=50 )
        
    # Image
    img= Image.open('Images/shot.png')
    img= img.resize((350, 300), Image.ANTIALIAS )
    img = ImageTk.PhotoImage(img)
    img_label = tk.Label(image=img)
    img_label.image = img
    
    forFrame1 = Label(frame1, image=img)
    
    
    
    # ------------------------ grid --------------------------------
    info_frame.grid(row=0,column=0, columnspan=2)
    forInfo_Frame.grid(row=0, column=0)
    
    frame.grid(row=1,column=0)
    forFrameTeste.grid(row=1, column=0)

    frame1.grid(row=1,column=1)
    forFrame1.grid(row=0, column=0)


def delete_all():
    
    for widget in validation1.winfo_children():
        widget.grid_forget()

    for widget in validation2.winfo_children():
        widget.grid_forget()
    

btnSubmit_toVal2 = Button(validation1, text="Next frame", command=val2)      

validation2 = Frame(validation1)
# ------------------------------------------------------------------


#------------------------Fail popup---------------------------------

# def popup():
#     # pode-se ter showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
#     messagebox.showinfo("ERROR!", "This is not in the system!")

# Button(validation1, text="Popup", command=popup).grid(row=4, column=3)

#-------------------------------------------------------------------


#------------------Posições no ecrã---------------------------------
logo_label.grid(row=0, column=0,padx=40, pady=40)
instructions.grid(row=1, column=1, padx=175, pady=20)
btnSubmit_toVal2.grid(row=4, column=1)





validation1.mainloop()