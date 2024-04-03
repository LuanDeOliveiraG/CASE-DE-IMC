import customtkinter as ctk
from tkinter import *

def imc():
    p = float(peso.get())
    a = float(altura.get())

    imc = round((p * (a * a))/10 , 2)

    if imc < 18.5 :
        info = 'Abaixo do peso \n'
    elif imc > 18.6 and imc < 24.9:
        info = 'Peso ideal \n'
    elif imc > 25.0 and imc < 29.9:
        info = 'Levemente acima do peso \n'
    elif imc > 30.0 and imc < 34.9:
        info = 'Obesidade Grau 1 \n'
    elif imc > 35.0 and imc < 39.9:
        info = 'Obesidade Grau 2 (Severa) \n'
    elif imc > 40.0:
        info = 'Obesidade 3 (Mórbida) \n'
        
    complemento = f'Seu IMC é {imc}''\n'

    Resultado.configure(text=str(info + complemento)) # aqui usa-se o configure para que no momento em que clicar na ação do botão, ele altere o texto

janela = ctk.CTk('#000000')
janela.geometry('500x500')
janela.resizable(False, False)
janela.title('Calculadora de IMC')

titulo=ctk.CTkLabel(janela,
                   width= 200, 
                   height= 50,
                   text= 'Calculadora de IMC',
                   font=('arial bold',20)).place(x= 150 , y = 20)

peso = ctk.CTkEntry(janela,
                        placeholder_text='Insira seu peso',
                        border_color='#0000CD')
peso.place(x=175, y=170)

altura = ctk.CTkEntry(janela,
                        placeholder_text='Insira sua altura em cm',
                        border_color='#0000CD')
altura.place(x=175, y=200)

btn = ctk.CTkButton(janela,
                    text="Calcular",
                    width=50,
                    height=50,
                    command=imc).place(x=320, y=175)

backgroung = ctk.CTkFrame(janela,
             width= 400,
             height= 150,
             fg_color='gray').place(x = 50, y= 230)
Resultado = ctk.CTkLabel(backgroung,
                   width= 200, 
                   height= 50,
                   text= 'Insira o peso e a altura em M com o ponto \n Ex.: 1.70',
                   font=('arial bold',20),
                   bg_color='gray')
Resultado.place(x = 60, y= 270)



janela.mainloop()