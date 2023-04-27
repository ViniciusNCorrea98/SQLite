from tkinter import *
from tkcalendar import Calendar, DateEntry
from tkinter import ttk
from tkinter import messagebox

#importando dados view.py
from view import *



co0 = "#f0f3f5"
co1 = "#feffff"
co2 = "#4fa882"
co3 = "#38576b"
co4 = "#403d3d"
co5 = "#e06636"
co6 = "#038cfc"
co7 = "#ef5350"
co8 = "#263238"
co9 = "#e9edf5"

#Criando janela

janela = Tk()
janela.title("")
janela.geometry('1043x453')
janela.configure(background=co9)
#Para travar a altura e comprimento da janela
janela.resizable(width=FALSE, height=FALSE)

frame_top = Frame(janela, width=310, height=50, bg=co2, relief='flat')
frame_top.grid(row=0, column=0)

frame_bottom = Frame(janela, width=310, height=400, bg=co1, relief='flat')
frame_bottom.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_right= Frame(janela, width=588, height=403, bg=co1, relief='flat')
frame_right.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

#Label Top
app_nome = Label(frame_top, text='Formulário de Consultoria', anchor=NW, font=('Ivy 13 bold'),bg=co2, fg=co1,relief='flat')
app_nome.place(x=10, y=20)


global tree
# Função inserir dados

def inserir():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    data_em = entry_data_consulta.get()
    estado = entry_estado_consulta.get()
    assunto = entry_assunto.get()

    lista = [nome, email, telefone, data_em, estado, assunto]

    if nome == '':
        messagebox.showerror('Erro', 'O campo nome é obrigatório!')
    elif email =='':
        messagebox.showerror('Erro', 'O campo email é obrigatório!')
    elif telefone == '':
        messagebox.showerror('Erro', 'O campo telefone é obrigatório!')
    elif data_em == '':
        messagebox.showerror('Erro', 'O campo Data é obrigatório!')
    elif estado == '':
        messagebox.showerror('Erro', 'O campo Estado é obrigatório!')
    elif assunto == '':
        messagebox.showerror('Erro', 'O campo Assunto é obrigatório!')
    else:
        inserir_info(lista)
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso!')

        entry_nome.delete(0, 'end')
        entry_email.delete(0, 'end')
        entry_telefone.delete(0, 'end')
        entry_data_consulta.delete(0, 'end')
        entry_estado_consulta.delete(0, 'end')
        entry_assunto.delete(0, 'end')

    for widget in frame_right.winfo_children():
        widget.destroy()

    mostar_tabela()



        #Configurando o Frame Bottom


#Função atualizar
def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = tree_lista[0]

        entry_nome.delete(0, 'end')
        entry_email.delete(0, 'end')
        entry_telefone.delete(0, 'end')
        entry_data_consulta.delete(0, 'end')
        entry_estado_consulta.delete(0, 'end')
        entry_assunto.delete(0, 'end')

        entry_nome.insert(0, tree_lista[1])
        entry_email.insert(0, tree_lista[2])
        entry_telefone.insert(0, tree_lista[3])
        entry_data_consulta.insert(0, tree_lista[4])
        entry_estado_consulta.insert(0, tree_lista[5])
        entry_assunto.insert(0, tree_lista[6])

        def update():
            nome = entry_nome.get()
            email = entry_email.get()
            telefone = entry_telefone.get()
            data_em = entry_data_consulta.get()
            estado = entry_estado_consulta.get()
            assunto = entry_assunto.get()

            lista = [nome, email, telefone, data_em, estado, assunto,valor_id]

            if nome == '':
                messagebox.showerror('Erro', 'O campo nome é obrigatório!')
            elif email == '':
                messagebox.showerror('Erro', 'O campo email é obrigatório!')
            elif telefone == '':
                messagebox.showerror('Erro', 'O campo telefone é obrigatório!')
            elif data_em == '':
                messagebox.showerror('Erro', 'O campo Data é obrigatório!')
            elif estado == '':
                messagebox.showerror('Erro', 'O campo Estado é obrigatório!')
            elif assunto == '':
                messagebox.showerror('Erro', 'O campo Assunto é obrigatório!')
            else:
                atualizar_info(lista)
                messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso!')

                entry_nome.delete(0, 'end')
                entry_email.delete(0, 'end')
                entry_telefone.delete(0, 'end')
                entry_data_consulta.delete(0, 'end')
                entry_estado_consulta.delete(0, 'end')
                entry_assunto.delete(0, 'end')

            for widget in frame_right.winfo_children():
                widget.destroy()

            mostar_tabela()

        botao_confirmar = Button(frame_bottom, text='CONFIRMAR', command=update, width=9, font=('Ivy 8 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
        botao_confirmar.place(x=108, y=340)

    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')

#Função deletar
def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = [tree_lista[0]]

        deletar_info(valor_id)
        messagebox.showinfo('Sucessso', 'Os dados foram deletados com sucesso!')

        for widget in frame_right.winfo_children():
            widget.destroy()

        mostar_tabela()

    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')


label_nome = Label(frame_bottom, text='Nome *', anchor=NW, font=('Ivy 10 bold'),bg=co1, fg=co4,relief='flat')
label_nome.place(x=10, y=10)

entry_nome = Entry(frame_bottom,width=45 ,justify='left' ,relief='solid')
entry_nome.place(x=5, y=40)

label_email = Label(frame_bottom, text='email *', anchor=NW, font=('Ivy 10 bold'),bg=co1, fg=co4,relief='flat')
label_email.place(x=8, y=70)

entry_email = Entry(frame_bottom, width=45, justify='left', relief='solid')
entry_email.place(x=5, y=100)

label_telefone = Label(frame_bottom, text='telefone *', anchor=NW, font=('Ivy 10 bold'),bg=co1, fg=co4,relief='flat')
label_telefone.place(x=8, y=130)

entry_telefone = Entry(frame_bottom, width=45, justify='left', relief='solid')
entry_telefone.place(x=5, y=160)


label_data_consulta = Label(frame_bottom, text='Data da consulta *', anchor=NW, font=('Ivy 10 bold'),bg=co1, fg=co4,relief='flat')
label_data_consulta.place(x=3, y=190)

entry_data_consulta = DateEntry(frame_bottom, width=18, background='darkblue', foreground='white', borderwidth=2)
entry_data_consulta.place(x=5, y=212)

label_estado_consulta = Label(frame_bottom, text='Estado da consulta *', anchor=NW, font=('Ivy 10 bold'),bg=co1, fg=co4,relief='flat')
label_estado_consulta.place(x=157, y=190)
#
entry_estado_consulta = Entry(frame_bottom, width=18, justify='left', relief='solid')
entry_estado_consulta.place(x=160, y=212)

label_assunto = Label(frame_bottom, text='Consulta sobre *', anchor=NW, font=('Ivy 10 bold'),bg=co1, fg=co4,relief='flat')
label_assunto.place(x=8, y=240)

entry_assunto = Entry(frame_bottom, width=45, justify='left', relief='solid')
entry_assunto.place(x=5, y=262)

#Criando botões no frame bottom
botao_inserir = Button(frame_bottom, command=inserir ,text='INSERIR',width=9,  font=('Ivy 8 bold'), bg=co6, fg=co1, relief='raised', overrelief='ridge')
botao_inserir.place(x=8, y=308)

botao_atualizar = Button(frame_bottom, command=atualizar,text='ATUALIZAR',width=9,  font=('Ivy 8 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
botao_atualizar.place(x=102, y=308)

botao_deletar = Button(frame_bottom, command=deletar,text='DELETAR',width=9,  font=('Ivy 8 bold'), bg=co7, fg=co1, relief='raised', overrelief='ridge')
botao_deletar.place(x=198, y=308)

#Frame Right
def mostar_tabela():
    global tree
    lista = mostrar_info()

    header_table = ['ID', 'Nome', 'email', 'Telefone','Data', 'Estado', 'Sobre']

    #Configurando a Tabela
    tree = ttk.Treeview(frame_right, selectmode='extended', columns=header_table, show='headings')

    #Criando o scroll vertical
    scroll_eixoY = ttk.Scrollbar(frame_right, orient='vertical', command=tree.yview)

    #Criando o scroll horizontal
    scroll_eixoX = ttk.Scrollbar(frame_right, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=scroll_eixoY.set, xscrollcommand=scroll_eixoX.set)
    tree.grid(column=0, row=0, sticky='nsew')
    scroll_eixoY.grid(column=1, row=0, sticky='ns')
    scroll_eixoX.grid(column=0, row=1, sticky='ew')
    frame_right.grid_rowconfigure(0, weight=12)

    #Dados de como os titulos da tabela ficaram centralizados
    hd=['nw', 'nw', 'nw', 'nw', 'center', 'center', 'center']
    #Dados dos comprimento das colunas tabela
    h=[30, 170, 140, 100, 100, 70, 100]
    i=0

    for col in header_table:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[i], anchor=hd[i])
        i+=1
    for item in lista:
        tree.insert('', 'end', values=item)


mostar_tabela()
janela.mainloop()