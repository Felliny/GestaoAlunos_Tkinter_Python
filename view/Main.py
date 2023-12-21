import tkinter
from datetime import datetime
from tkinter import *
from tkinter import ttk, messagebox

from controller.GestaoAlunosController import GestaoAlunosController

controller = GestaoAlunosController()


def clickBtnConfirmar():
    ra = entryRa.get()
    nome = entryNome.get()
    nascimento = entryNascimento.get()
    try:
        data_formatada = datetime.strptime(nascimento, "%d/%m/%Y")
    except ValueError:
        messagebox.showinfo("Erro", "Digite a data nesse formato: 15/03/2003")
    else:
        controller.cadastrar(ra, nome, nascimento)
        populateTable()

        entryRa.delete(0, END)
        entryNome.delete(0, END)
        entryNascimento.delete(0, END)


def clickBtnApagar():
    ra = entryRa.get()

    controller.remover(ra)

    populateTable()

    entryRa.delete(0, END)
    entryNome.delete(0, END)
    entryNascimento.delete(0, END)


def clickBtnPesquisar():
    ra = entryRa.get()

    controller.pesquisar(ra)

    entryRa.delete(0, END)
    entryNome.delete(0, END)
    entryNascimento.delete(0, END)

    entryRa.insert(0, ra)
    entryNome.insert(0, controller.nome)
    entryNascimento.insert(0, controller.nascimento)

    controller.limparDados()

def populateTable():
    children = tv.get_children()
    for item in children:
        tv.delete(item)
    for aluno in controller.alunos:
        tv.insert("", "end", values=(aluno.ra, aluno.nome, aluno.nascimento))


window = Tk()  # Instacia uma instância de janela
window.geometry("600x420")
window.title("Gestão de Alunos")


window.config(background="black")

labelNome = Label(window, text="Nome:",
                  font=('Arial', 18, 'bold'),
                  fg='#00FF00',
                  bg='black')
labelRa = Label(window, text="RA:",
                font=('Arial', 18, 'bold'),
                fg='#00FF00',
                bg='black')

labelNascimento = Label(window, text="Data de Nascimento:",
                        font=('Arial', 18, 'bold'),
                        fg='#00FF00',
                        bg='black')

btnConfirmar = Button(window, text="Cadastrar", command=clickBtnConfirmar,
                      font=("Comic Sans", 20),
                      fg='#00FF00',
                      bg='black',
                      activebackground='black',
                      activeforeground='#00FF00')

btnApagar = Button(window, text="Remover", command=clickBtnApagar, font=("Comic Sans", 20), fg='#00FF00',
                   bg='black',
                   activebackground='black',
                   activeforeground='#00FF00')

btnPesquisar = Button(window, text="Pesquisar", command=clickBtnPesquisar, font=("Comic Sans", 20), fg='#00FF00',
                      bg='black',
                      activebackground='black',
                      activeforeground='#00FF00')

entryNome = Entry(window,
                  font=("Arial", 18))

entryRa = Entry(window, font=("Arial", 18))

entryNascimento = Entry(window, font=("Arial", 18))

tv = ttk.Treeview(window, columns=('ra', 'nome', 'data'), show='headings')
tv.column('ra', minwidth=0, width=50, anchor=tkinter.CENTER)
tv.column('nome', minwidth=0, width=150, anchor=tkinter.CENTER)
tv.column('data', minwidth=0, width=150, anchor=tkinter.CENTER)
tv.heading('ra', text="RA")
tv.heading('nome', text="Nome")
tv.heading('data', text="Data de Nascimento")

tv.place(x=0, y=200)

labelRa.grid(row=0, column=0)
labelNome.grid(row=1, column=0)
labelNascimento.grid(row=2, column=0)
entryRa.grid(row=0, column=1)
entryNome.grid(row=1, column=1)
entryNascimento.grid(row=2, column=1)
btnConfirmar.place(x=0, y=110)
btnApagar.place(x=282, y=110)
btnPesquisar.place(x=140, y=110)

window.mainloop()  # Mostra a tela na tela do computador
