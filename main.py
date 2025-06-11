import tkinter as tk
from tkinter import filedialog
from bibliotecas import enzimas

def capturaDados(entrada, resultado): 
    sequencia = entrada.get().strip().replace("\n","").replace(" ","").replace(",","").replace(".","").replace(";","").replace("?","").upper()
    valido = True
    bases_esperadas = ["A","T","C","G"]
    bases_rna = ["A", "U", "C", "G"]
    for letra in sequencia:
        if (letra not in bases_esperadas) and (letra not in bases_rna):
            valido = False
            break
    if valido is True:
        if "U" in sequencia:
            sequencia = sequencia.replace("U", "T")
            with open("assets/sequencia.txt", "w") as f:
                f.write(sequencia)
            saida = f"Sequência de RNA identificada e convertida em sequência de DNA: {sequencia}"
        else:
            with open("assets/sequencia.txt", "w") as f:
                f.write(sequencia)
            saida = f"Sequência armazenada: {sequencia}"
    else:
        saida = "Base inesperada identificada. Revise a sua sequência."
    resultado.config(text=saida)

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
    
def gera_fita_complementar(sequencia):
    complementares = {
        'A' : 'T',
        'T' : 'A',
        'C' : 'G',
        'G' : 'C',
    }

    fita_complementar = []

    for base in sequencia:
        fita_complementar.append(complementares[base])

    return ''.join(fita_complementar)

def calcular_gc(sequencia):
    gc = sequencia.count("G") + sequencia.count("C")
    return gc

def Temperatura_Melting(sequencia):
    gc = calcular_gc(sequencia)
    total = len(sequencia)
    melting = 64.9 + 41 * (gc- 16.4) / total
    return melting

def enzimas_de_restricao(sequencia):
    enzimas_restricao_presentes = {}
    enzimas_restricao_lista = []
    for nome_enzima, seq_enzima in enzimas.items():
        if seq_enzima in sequencia:
            enzimas_restricao_lista.append(nome_enzima)
            if nome_enzima not in enzimas_restricao_presentes.keys():
                enzimas_restricao_presentes[nome_enzima] = sequencia.count(seq_enzima)
    # em tabela - fazer uma mais bonitinha?
    enzimas_restricao_tabela = "Enzima\tFrequência"
    for enzima, frequencia in enzimas_restricao_presentes.items():
        enzimas_restricao_tabela += f"\n{enzima}\t{frequencia}"
    return enzimas_restricao_tabela
