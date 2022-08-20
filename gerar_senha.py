import random
from tkinter import *
from tkinter import messagebox
import pyperclip

gui = Tk()
gui.title('Gerador de Senha')
gui.geometry('300x100')
gui.resizable(0,0)

def gerar_senha():
    tamanho = int(passar_string.get())

    letras_minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letras_maisculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    tudo = letras_minusculas + letras_maisculas + numeros
    aleatorio = random.sample(tudo, tamanho)
    senha = "".join(aleatorio)
    messagebox.showinfo("Resultado", f"Senha: {senha} \n\nSenha copiada para área de transferência")
    pyperclip.copy(senha)

passar_string = StringVar()
texto1 = Label(text="Informe o tamanho da senha").pack(pady=10)
texto2 = Entry(textvariable=passar_string).pack()
botao = Button(text="Gerar", command=gerar_senha).pack(pady=10)

gui.mainloop()