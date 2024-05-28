# Importando tkinter
from tkinter import *
from tkinter import Tk, StringVar, ttk, messagebox
from tkinter import filedialog as fd

# Importando pillow
from PIL import Image, ImageTk

# Importando Tkcalendar
from tkcalendar import Calendar, DateEntry
from datetime import date, datetime

# Importando funções da view
from view import *

global tree

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
janela.geometry('1200x600')
janela.configure(background=verde_escuro)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

# Criando frames
frame_topo = Frame(janela, width=1200, height=50, bg=branco, relief=FLAT)
frame_topo.grid(row=0, column=0)

frame_meio = Frame(janela, width=1200, height=300, bg=branco, pady=20, relief=FLAT)
frame_meio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=1200, height=300, bg=branco, relief=FLAT)
frame_baixo.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

# Criando funções
# Função inserir
def inserir():
    global imagem, imagem_string, l_imagem
    nome = e_nome.get()
    local = e_local.get()
    descricao = e_desc.get()
    marca = e_marca.get()
    data = e_cal.get()
    valor = e_valor.get()
    serie = e_serie.get()
    imagem = imagem_string

    lista_inserir = [nome, local, descricao, marca, data, valor, serie, imagem]

    for i in lista_inserir:
        if i == '':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return

    inserir_dados(lista_inserir)

    messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

    # Limpando os campos
    e_nome.delete(0, 'end')
    e_local.delete(0, 'end')
    e_desc.delete(0, 'end')
    e_marca.delete(0, 'end')
    e_cal.delete(0, 'end')
    e_valor.delete(0, 'end')
    e_serie.delete(0, 'end')

    mostrar()

# Função atualizar
def atualizar():
    global imagem, imagem_string, l_imagem
    try:
        # Pegando dados da linha selecionada na tabela
        tree_ver_dados = tree.focus()
        tree_ver_dicionario = tree.item(tree_ver_dados)
        tree_ver_lista = tree_ver_dicionario['values']

        valor = tree_ver_lista[0]

        # Limpando os campos
        e_nome.delete(0, 'end')
        e_local.delete(0, 'end')
        e_desc.delete(0, 'end')
        e_marca.delete(0, 'end')
        e_cal.delete(0, 'end')
        e_valor.delete(0, 'end')
        e_serie.delete(0, 'end')

        # Inserindo dados nos campos
        id = int(tree_ver_lista[0])
        e_nome.insert(0, tree_ver_lista[1])
        e_local.insert(0, tree_ver_lista[2])
        e_desc.insert(0, tree_ver_lista[3])
        e_marca.insert(0, tree_ver_lista[4])
        e_cal.insert(0, tree_ver_lista[5])
        e_valor.insert(0, tree_ver_lista[6])
        e_serie.insert(0, tree_ver_lista[7])
        imagem_string = tree_ver_lista[8]

        def update():
            global imagem, imagem_string, l_imagem

            nome = e_nome.get()
            local = e_local.get()
            descricao = e_desc.get()
            marca = e_marca.get()
            data = e_cal.get()
            valor = e_valor.get()
            serie = e_serie.get()
            imagem = imagem_string

            if imagem == '':
                e_serie.insert(0, tree_ver_lista[8])

            lista_atualizar = [nome, local, descricao, marca, data, valor, serie, imagem, id]

            for i in lista_atualizar:
                if i == '':
                    messagebox.showerror('Erro', 'Preencha todos os campos')
                    return

            atualizar_dados(lista_atualizar)
            messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')

            # Limpando os campos
            e_nome.delete(0, 'end')
            e_local.delete(0, 'end')
            e_desc.delete(0, 'end')
            e_marca.delete(0, 'end')
            e_cal.delete(0, 'end')
            e_valor.delete(0, 'end')
            e_serie.delete(0, 'end')

            b_confirmar.destroy()
            mostrar()

        # Botão confirmar atualização
        b_confirmar = Button(frame_meio, command=update, text='Confirmar'.upper(), width=61, overrelief=RIDGE, bg=branco, fg=cor_letra)
        b_confirmar.place(x=130, y=243)

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um item da tabela')

# Função deletar
def deletar():
    try:
        # Pegando dados da linha selecionada na tabela
        tree_ver_dados = tree.focus()
        tree_ver_dicionario = tree.item(tree_ver_dados)
        tree_ver_lista = tree_ver_dicionario['values']

        valor = tree_ver_lista[0]

        deletar_dados([valor])

        messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')
        mostrar()

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um item da tabela')


# Função para escolher imagem
def escolher_imagem():
    global imagem, imagem_string, l_imagem
    imagem = fd.askopenfilename()
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((170, 170))
    imagem = ImageTk.PhotoImage(imagem)

    l_img = Label(frame_meio, image=imagem, bg=branco, fg=verde)
    l_img.place(x=900, y=10)

# Função para ver imagem
def ver_imagem():
    global imagem, imagem_string, l_imagem

    # Pegando dados da linha selecionada na tabela
    tree_ver_dados = tree.focus()
    tree_ver_dicionario = tree.item(tree_ver_dados)
    tree_ver_lista = tree_ver_dicionario['values']

    valor = [int(tree_ver_lista[0])]

    item = ver_dados_individuais(valor)

    imagem = item[0][8]

    imagem = Image.open(imagem)
    imagem = imagem.resize((170, 170))
    imagem = ImageTk.PhotoImage(imagem)

    l_img = Label(frame_meio, image=imagem, bg=branco, fg=verde)
    l_img.place(x=900, y=10)


# Trabalhando no frame do topo
# Abrindo imagem
logo_img = Image.open('logo.png')
logo_img = logo_img.resize((45, 45))
logo_img = ImageTk.PhotoImage(logo_img)

logo = Label(frame_topo, image=logo_img, text=' Inventário', width=1200, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=branco, fg=cor_letra)
logo.place(x=0, y=0)

# Trabalhando no frame do meio
# Criando entradas
# Nome
l_nome = Label(frame_meio, text='Nome', height=1, anchor=NW, bg=branco, fg=cor_letra)
l_nome.place(x=10, y=5)

e_nome = Entry(frame_meio, width=30, justify='left', relief=SOLID)
e_nome.place(x=130, y=6)

# Localização
l_local = Label(frame_meio, text='Local', height=1, anchor=NW, bg=branco, fg=cor_letra)
l_local.place(x=10, y=30)

e_local = Entry(frame_meio, width=30, justify='left', relief=SOLID)
e_local.place(x=130, y=31)

# Descrição
l_desc = Label(frame_meio, text='Descrição', height=1, anchor=NW, bg=branco, fg=cor_letra)
l_desc.place(x=10, y=55)

e_desc = Entry(frame_meio, width=30, justify='left', relief=SOLID)
e_desc.place(x=130, y=56)

# Marca
l_marca = Label(frame_meio, text='Marca', height=1, anchor=NW, bg=branco, fg=cor_letra)
l_marca.place(x=10, y=85)

e_marca = Entry(frame_meio, width=30, justify='left', relief=SOLID)
e_marca.place(x=130, y=86)

# Data
l_cal = Label(frame_meio, text='Data da Compra', height=1, anchor=NW, bg=branco, fg=cor_letra)
l_cal.place(x=10, y=115)

e_cal = DateEntry(frame_meio, width=28, Background='darkblue', bordewidth=2, year=datetime.now().year, relief=SOLID)
e_cal.place(x=130, y=116)

# Valor da Compra
l_valor = Label(frame_meio, text='Valor da Compra', height=1, anchor=NW, bg=branco, fg=cor_letra)
l_valor.place(x=10, y=145)

e_valor = Entry(frame_meio, width=30, justify='left', relief=SOLID)
e_valor.place(x=130, y=146)

# Número de série
l_serie = Label(frame_meio, text='Número de Série', height=1, anchor=NW, bg=branco, fg=cor_letra)
l_serie.place(x=10, y=175)

e_serie = Entry(frame_meio, width=30, justify='left', relief=SOLID)
e_serie.place(x=130, y=176)

# Imagem do item
# Botão carregar
l_item = Label(frame_meio, text='Imagem do item', height=1, anchor=NW, bg=branco, fg=cor_letra)
l_item.place(x=10, y=205)

b_carregar = Button(frame_meio, command=escolher_imagem, text='Carregar'.upper(), width=29, compound=CENTER, anchor=CENTER, overrelief=RIDGE, bg=branco, fg=cor_letra)
b_carregar.place(x=130, y=205)

# Botão inserir
b_inserir = Button(frame_meio, command=inserir, text='Adicionar'.upper(), width=29, compound=CENTER, anchor=CENTER, overrelief=RIDGE, bg=branco, fg=cor_letra)
b_inserir.place(x=385, y=5)

# Botão Atualizar
b_update = Button(frame_meio, command=atualizar, text='Atualizar'.upper(), width=29, compound=CENTER, anchor=CENTER, overrelief=RIDGE, bg=branco, fg=cor_letra)
b_update.place(x=385, y=45)

# Botão Deletar
b_deletar = Button(frame_meio, command=deletar, text='Deletar'.upper(), width=29, compound=CENTER, anchor=CENTER, overrelief=RIDGE, bg=branco, fg=cor_letra)
b_deletar.place(x=385, y=85)

# Botão Ver Item
b_ver_item = Button(frame_meio, command=ver_imagem, text='Ver Item'.upper(), width=29, compound=CENTER, anchor=CENTER, overrelief=RIDGE, bg=branco, fg=cor_letra)
b_ver_item.place(x=385, y=205)

# Labels Quantidade Total e Valores
# Total
l_total = Label(frame_meio, text='', height=3, width=25, pady=20, anchor=CENTER, bg=ciano, fg=branco)
l_total.place(x=650, y=7)

l_valor_total = Label(frame_meio, text='Valor Total dos Itens', width=25, height=1, anchor=NW, bg=ciano, fg=branco)
l_valor_total.place(x=650, y=5)

l_qtd = Label(frame_meio, text='', height=3, width=25, pady=20, anchor=CENTER, bg=ciano, fg=branco)
l_qtd.place(x=650, y=133)

l_qtd_total = Label(frame_meio, text='Quantidade de itens', width=25, height=1, anchor=NW, bg=ciano, fg=branco)
l_qtd_total.place(x=650, y=135)

# Trabalhando no frame de baixo

def mostrar():
    global tree

    # Criando a tabela
    tabela_head = ['#ID', 'Nome', 'Local', 'Descrição', 'Marca', 'Data da Compra', 'Valor da Compra', 'Número de Série']

    lista_itens = ver_todos_dados()

    tree = ttk.Treeview(frame_baixo, selectmode='extended', columns=tabela_head, show='headings')

    # Scrollbar vertical
    vsb = ttk.Scrollbar(frame_baixo, orient='vertical', command=tree.yview)

    # Scrollbar horizontal
    hsb = ttk.Scrollbar(frame_baixo, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frame_baixo.grid_rowconfigure(0, weight=12)

    hd = ['center', 'center', 'center', 'center', 'center', 'center', 'center', 'center']
    h = [40, 150, 125, 260, 130, 160, 160, 160]
    n = 0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n], anchor=hd[n])

        n += 1

    # Inserindo itens na tabela
    for item in lista_itens:
        tree.insert('', 'end', values=item)

    # Calculando valor total e total de itens
    quantidade = []
    for item in lista_itens:
        quantidade.append(item[6])

    total_valor = sum(quantidade)
    total_itens = len(quantidade)

    # Atualizando os textos das labels
    l_total['text'] = f'R$ {total_valor:,.2f}'
    l_qtd['text'] = total_itens

mostrar()

janela.mainloop()
