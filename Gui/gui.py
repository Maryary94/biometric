import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
import os
from tkinter.constants import N, SUNKEN, S
from PIL import Image, ImageTk



gui =tk.Tk()
#-------------estrutura da aplicação, color e icon------------------
gui.title("Bio application")
gui.geometry('1280x720')
gui.config(bg='#263d42') 
gui.iconbitmap("Images/fingerprint2.ico")
#-------------------------------------------------------------------


#----------------------------logotipo-------------------------------
logo = Image.open('Images/biom.png')
logo= logo.resize((150, 200), Image.ANTIALIAS )
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
#-------------------------------------------------------------------

# # Informação
instructions = tk.Label(gui,text="Insert your CompanyID",font=("Arial", 25))

#-------------------------input CompanyID---------------------------
e = Entry(gui, width=50, borderwidth=2,font=("Arial", 15), relief="flat")

#-------------------------------------------------------------------

#-------------------------função do botão---------------------------
def btnClick():
    btnLabel= Label(gui, text=e.get())
    btnLabel.grid(row=4, column=0)

btnSubmit = Button(gui, text="Start Registration", command=btnClick,font=("Arial", 18))
#-------------------------------------------------------------------





# --------------------- Frames -------------------------------------

def toReg1():
    delete_all()
    registration1.grid(row=0, column=0, padx=35, pady=30)
    
    info_frame = LabelFrame(registration1, padx=470, pady=50 )
    forInfo_Frame = Label(info_frame, text="Adicionar Instruções",padx=15, pady=15,font=("Arial", 18))
    
    frame = LabelFrame(registration1, text="video of the user", padx=50, pady=50 )
    
    
    # Para se mudar para o video
    testeImageToChangeToVideo= Image.open('Images/bio-info.png')
    testeImageToChangeToVideo= testeImageToChangeToVideo.resize((350, 300), Image.ANTIALIAS )
    testeImageToChangeToVideo = ImageTk.PhotoImage(testeImageToChangeToVideo)
    img_label = tk.Label(image=testeImageToChangeToVideo)
    img_label.image = testeImageToChangeToVideo
    forFrameTeste = Label(frame, image=testeImageToChangeToVideo)
    
    # forFrame = Label(frame, text="frame!",padx=5, pady=15)
    
    
    
    
    
    
    frame1 = LabelFrame(registration1, padx=50, pady=50 )
        
    # Image
    img= Image.open('Images/shot.png')
    img= img.resize((350, 300), Image.ANTIALIAS )
    img = ImageTk.PhotoImage(img)
    img_label = tk.Label(image=img)
    img_label.image = img
    
    forFrame1 = Label(frame1, image=img)
    
  
    

    
    # ----------------------- Next frame ---------------------------
    
    btnNext = Button(registration1, text="Next frame", command=toReg2)      
    btnNext.grid(row=4, column=1)
    
    
    # ------------------------ grid --------------------------------
    info_frame.grid(row=0,column=0, columnspan=2)
    forInfo_Frame.grid(row=0, column=0)
    
    frame.grid(row=1,column=0)
    forFrameTeste.grid(row=1, column=0)
    # forFrame.grid(row=2, column=0)
    
    frame1.grid(row=1,column=1)
    forFrame1.grid(row=0, column=0)
    


def toReg2():
    delete_all()
    registration2.grid(row=0, column=0, padx=35, pady=30)
    
    info_frame = LabelFrame(registration2, padx=470, pady=50 )
    forInfo_Frame = Label(info_frame, text="Adicionar Instruções",padx=15, pady=15,font=("Arial", 18))
    
    frame = LabelFrame(registration2,  padx=50, pady=50 )
    
    imageInstructions= Image.open('Images/cringe.png')
    imageInstructions= imageInstructions.resize((350, 300), Image.ANTIALIAS )
    imageInstructions = ImageTk.PhotoImage(imageInstructions)
    img_label = tk.Label(image=imageInstructions)
    img_label.image = imageInstructions
    forFrame = Label(frame, image=imageInstructions)
    
    
    # ------------------------ grid --------------------------------
    info_frame.grid(row=0,column=0, columnspan=3)
    forInfo_Frame.grid(row=0, column=0)
    
    frame.grid(row=1,column=1)
    forFrame.grid(row=1, column=1)


# ------------------ delete frames ---------------------------------
def delete_all():
    # print(registration1.winfo_children() , "interface")
    # print(registration2.winfo_children(), "interface2")
    
    for widget in gui.winfo_children():
        widget.grid_forget()

    for widget in registration1.winfo_children():
        widget.grid_forget()
    
    for widget in registration2.winfo_children():
        widget.grid_forget()  

 

btnSubmit_toReg1 = Button(gui, text="Next frame", command=toReg1)      

registration1 = Frame(gui)
registration2 = Frame(gui)

# ------------------------------------------------------------------


#------------------Posições no ecrã---------------------------------
logo_label.grid(row=0, column=0,padx=40, pady=40)
instructions.grid(row=1, column=1)
e.grid(row=2, column=1, padx=125, pady=20)
btnSubmit.grid(row=3, column=1, pady=40)
btnSubmit_toReg1.grid(row=4, column=1) 



gui.mainloop()