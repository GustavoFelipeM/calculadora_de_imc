from customtkinter import *
import customtkinter as ctk

#Função para calcular IMC
def resultado():
    num1= int(entrada.get())
    num2= int(entrada2.get())
    cm = num2/100
    r= num1/(cm**2)
    
    if r <= 19:
        lb = ctk.CTkLabel(root,text="Abaixo do peso", text_color="white",bg_color="#3b3c36",text_font="Arial 12 bold")
        lb.place(x=182, y=200)
    elif r >= 19 and r<=25:
        lb = ctk.CTkLabel(root,text="Peso normal", text_color="white",bg_color="#3b3c36",text_font="Arial 12 bold")
        lb.place(x=182, y=200)
    elif r >= 25 and r <=30:
        lb = ctk.CTkLabel(root,text="Sobrepeso", text_color="white",bg_color="#3b3c36",text_font="Arial 12 bold")
        lb.place(x=182, y=200)
    elif r >= 30 and r <=35:
        lb = ctk.CTkLabel(root,text="Obesidade I", text_color="white",bg_color="#3b3c36",text_font="Arial 12 bold")
        lb.place(x=182, y=200)
    elif r >= 35 and r<=40:
        lb = ctk.CTkLabel(root,text="Obesidade II", text_color="white",bg_color="#3b3c36",text_font="Arial 12 bold")
        lb.place(x=182, y=200)
    elif r >= 40:
        lb = ctk.CTkLabel(root,text=" Obesidade \n mórbida", text_color="white",bg_color="#3b3c36",text_font="Arial 12 bold")
        lb.place(x=182, y=193)
    
    #Botão para resetar
    if r is not None:
        bo= ctk.CTkButton(root, text="Reset",command=lambda:[lb.destroy(), bo.destroy()], text_color="white", fg_color="red", text_font="arial 12 bold",hover_color="#C70000",height=14, width=20)
        bo.place(x= 370, y=106)

#Tela
root = CTk()
root.geometry("500x300")
root.configure(background="#327572")
root.resizable(False,False)
root.title("Calculadora de IMC")
root.iconbitmap("img/fita.ico")

#Textos
txt = CTkLabel(root, text="Calculadora de IMC", bg_color="#327572", text_color="white",text_font="Arial 18 bold")
txt2 = CTkLabel(root, text="Qual seu peso:                                      (kg)", bg_color="#327572", text_color="white",text_font="Arial 12 bold")
txt3 = CTkLabel(root, text="Qual sua altura:                                     (cm)", bg_color="#327572", text_color="white",text_font="Arial 12 bold")
txt4 = CTkLabel(root, text="Resultado: ", bg_color="#327572", text_color="white",text_font="Arial 12 bold")

#Frames
f1 = CTkFrame(root,width=450, fg_color="white")
f2 = CTkFrame(root,width=200, fg_color="#E0C02B")
f3 = CTkFrame(root,width=184, fg_color="#3b3c36",bg_color="#3b3c36")

#Entradas de dados
entrada = CTkEntry(root,text_font="arial 12 bold",placeholder_text=70)
entrada2 = CTkEntry(root,text_font="arial 12 bold",placeholder_text=170)

#Botão
b= CTkButton(root, text="Calcular",command=resultado, fg_color="white", text_color="#3b3c36", hover_color="#E0E0E0", text_font="arial 12 bold", height=14, width=20)

#places
txt.place(x=140,y=5)
txt2.place(x=35,y=100)
txt3.place(x=35,y=50)
txt4.place(x=125,y=140)
f1.place(x=25, y=38,height=5)
f2.place(x=150, y=165,height=100)
f3.place(x=158, y=173,height=85)
entrada.place(x=160,y=103)
entrada2.place(x=160,y=53)
b.place(x= 350, y=54)


root.mainloop()