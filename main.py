import tkinter as tk
from tkinter import filedialog

def capturaDados(entrada, resultado): 
    sequencia = entrada.get().strip().upper()
    with open("assets/sequencia.txt", "w") as f:
        f.write(sequencia)
    resultado.config(text=f"Sequência armazenada: {sequencia}")

    total = len(sequencia)

def carregaArquivo(entrada):
    path = filedialog.askopenfilename(
        title="Selecione o arquivo: ",
        filetypes=[
            ("Arquivos de texto", "*.txt *.fasta"),
            ("Todos os arquivos", "*.*")
            ]
            )
    
    if path:
        with open(path, "r") as f:
            content = f.read().strip().upper()

            #fasta 
            if content.startswith(">"):
                lines = content.splitlines()
                content = "".join(singleline for singleline in lines if not singleline.startswith(">"))
            entrada.delete(0, tk.END)
            entrada.insert(0, content)
    

def calcular_gc(sequencia):
    gc = sequencia_de_bases.count("G") + sequencia_de_bases.count("C")
    return gc

def Temperatura_Melting(sequencia):
    melting = 64.9 + 41 * (gc - 16.4) / total
    return melting
