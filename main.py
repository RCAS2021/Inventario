from tkinter import *
from tkinter import Tk, StringVar, ttk

# Cores
branco = "#feffff"
verde = "#4fa882"
cor_valor = "#38576b"
cor_letra = "#403d3d"
cor_lucro = "#e06636"
azul = "#038cfc"
ciano = "#3fbfb9"
verde_escuro = "#263238"

# Criando Janela
janela = Tk()
janela.title('Inventário')
janela.geometry('900x600')
janela.configure(background=verde_escuro)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

# Criando frames
frame_topo = Frame(janela, width=900, height=50, bg=branco, relief=FLAT)
frame_topo.grid(row=0, column=0)

frame_meio = Frame(janela, width=900, height=300, bg=branco, pady=20, relief=FLAT)
frame_meio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=900, height=300, bg=branco, relief=FLAT)
frame_baixo.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)

janela.mainloop()


