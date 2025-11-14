import ttkbootstrap as ttk
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
        self.janela.geometry("1500x900+230+70")

        #Titulo da pagina
        label_ttl = ttk.Label(self.janela, text="Sorteio de Frutas 🎰", font=("Broadway", 40)).pack(pady=10)
        
        frame_fruta = ttk.Frame(self.janela).pack(padx=10)

        #Frutas
        self.label_f1 = ttk.Label(frame_fruta, bootstyle="info", padding=10, relief="solid").pack(side="left", pady=15, padx=5)

        self.label_f2 = ttk.Label(frame_fruta, bootstyle="info", padding=10, relief="solid").pack(side="left", pady=15, padx=5)

        self.label_f3 = ttk.Label(frame_fruta, bootstyle="info", padding=10, relief="solid").pack(side="left", pady=15, padx=5)

        #Botão sorteio
        botao_sort = ttk.Button(self.janela, text="Sortear").pack(pady=20)


    def soreteio(self):
        pass






       








    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    pag = Jogo_Fruta()
    pag.run()
