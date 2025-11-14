import ttkbootstrap as ttk
import random
import sqlite3
import tkinter as tk
from tkinter import messagebox

#Lista de frutas
lista_frutas = ['🍇', '🍉', '🍓', '🍍', '🍒']

class Jogo_Fruta:

    def __init__(self):
        
        #Criando a janela
        self.janela = ttk.Window(themename="morph",
                                   title="Slot Machine")
        
        #Tamanho da janela
        self.janela.geometry("900x900+230+70")

        #Titulo da pagina
        label_ttl = ttk.Label(self.janela, text="Sorteio de Frutas 🎰", font=("Broadway", 40)).pack(pady=(10,0))
        
        frame_fruta = ttk.Frame(self.janela)
        frame_fruta.pack(pady=20)

        #Frutas
        #O bootstyle é para definir a cor da figura que está dentro da label
        #O relief="solid" é a borda da label
        self.label_f1 = ttk.Label(frame_fruta, text="🍇", font=("Arial", 64), bootstyle="primary", padding=10, relief="solid")
        self.label_f1.pack(side="left",padx=30)

        self.label_f2 = ttk.Label(frame_fruta, text="🍇", font=("Arial", 64), bootstyle="primary", padding=10, relief="solid")
        self.label_f2.pack(side="left",padx=30)

        self.label_f3 = ttk.Label(frame_fruta, text="🍇", font=("Arial", 64), bootstyle="primary", padding=10, relief="solid")
        self.label_f3.pack(side="left",padx=30)

        #Botão sorteio
        botao_sort = ttk.Button(self.janela, text="Sortear", command=self.soreteio).pack(pady=20, padx=5)

        #Treeview
        ttk.Label(self.janela, text="Histórico de Jogadas", font=("Broadway", 20)).pack(pady=(20, 10))

        tree = ttk.Treeview(self.janela,padding=90).pack()


    def soreteio(self):
        #Sortear a lista aleatoria
        f1 = random.choice(lista_frutas)
        f2 = random.choice(lista_frutas)
        f3 = random.choice(lista_frutas)

        #Atualizar o text da label para as frutas sorteadas 
        self.label_f1.config(text=f1)
        self.label_f2.config(text=f2)
        self.label_f3.config(text=f3)






       








    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    pag = Jogo_Fruta()
    pag.run()
