import tkinter as tk
from tkinter import messagebox

def atualizar_listas():
    lista_tarefas_pendentes.delete(0, tk.END)
    lista_tarefas_concluidas.delete(0, tk.END)
    for tarefa in tarefas_pendentes + tarefas_concluidas:
        lista_tarefas_pendentes.insert(tk.END, tarefa) if tarefa not in tarefas_concluidas else lista_tarefas_concluidas.insert(tk.END, tarefa)

def manipular_tarefa(acao):
    tarefa = entrada_tarefa.get().strip()
    try:
        tarefa_selecionada = lista_tarefas_pendentes.curselection()
        tarefa = lista_tarefas_pendentes.get(tarefa_selecionada) if tarefa == "" else tarefa
    except IndexError:
        tarefa_selecionada = None

    if acao == "adicionar" and tarefa: tarefas_pendentes.append(tarefa)
    elif acao == "excluir" and tarefa_selecionada: tarefas_pendentes.remove(tarefa)
    elif acao == "concluir" and tarefa_selecionada:
        tarefas_pendentes.remove(tarefa)
        tarefas_concluidas.append(tarefa)

    entrada_tarefa.delete(0, tk.END)
    atualizar_listas()

janela = tk.Tk()
janela.title("Lista de Tarefas Diárias")

tarefas_pendentes, tarefas_concluidas = [], []

entrada_tarefa = tk.Entry(janela, width=40)
entrada_tarefa.grid(row=0, column=0, padx=10, pady=10)

tk.Button(janela, text="Adicionar Tarefa", width=20, command=lambda: manipular_tarefa("adicionar")).grid(row=0, column=1, padx=10, pady=10)
lista_tarefas_pendentes = tk.Listbox(janela, height=10, width=50)
lista_tarefas_pendentes.grid(row=1, column=0, padx=10, pady=10)
lista_tarefas_concluidas = tk.Listbox(janela, height=10, width=50)
lista_tarefas_concluidas.grid(row=1, column=1, padx=10, pady=10)

tk.Button(janela, text="Excluir Tarefa", width=20, command=lambda: manipular_tarefa("excluir")).grid(row=2, column=0, padx=10, pady=10)
tk.Button(janela, text="Concluir Tarefa", width=20, command=lambda: manipular_tarefa("concluir")).grid(row=2, column=1, padx=10, pady=10)

atualizar_listas()

janela.mainloop()