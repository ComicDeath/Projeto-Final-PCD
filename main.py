import tkinter as tk
import matplotlib.pyplot as plt
from contagem_de_bases import calcular_gc, calcular_at
from tkinter import filedialog
from bibliotecas import enzimas

#VAR GLOBAL DA SEQUENCIA (MEGA HIPER IMPORTANTE)
sequencia = ""
def sequenciaVar(caminho):
    global sequencia
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            sequencia = f.read()
    except Exception as e:
        print(f"Erro ao ler a sequência do arquivo: {e}")
        sequencia = ""

def capturaDados(entrada, resultado): 
    sequencia_crua = entrada.get().strip().replace("\n","").replace(" ","").replace(",","").replace(".","").replace(";","").replace("?","").upper()
    valido = True
    bases_esperadas = ["A","T","C","G"]
    bases_rna = ["A", "U", "C", "G"]
    for letra in sequencia_crua:
        if letra not in bases_esperadas and letra not in bases_rna:
            valido = False
            break

    intervalo = 80
    pedacos = []
    for i in range(0, len(sequencia_crua), intervalo):
        pedacos.append(sequencia_crua[i:i+intervalo])
        sequencia_visualizacao = "\n".join(pedacos)
    
    if valido is True:
        if "U" in sequencia_crua:
            sequencia_crua = sequencia_crua.replace("U", "T")
            sequencia_visualizacao = sequencia_visualizacao.replace("U", "T")
            with open("assets/sequencia.txt", "w") as f:
                f.write(sequencia_crua)
            saida = f"Sequência de RNA identificada e armazenada como sequência de DNA:\n {sequencia_visualizacao}"
        else:
            with open("assets/sequencia.txt", "w") as f:
                f.write(sequencia_crua)
            saida = f"Sequência de DNA armazenada:\n {sequencia_visualizacao}"
    else:
        saida = "Base inesperada identificada. Revise a sua sequência."
    resultado.config(text=saida)

    sequenciaVar("assets/sequencia.txt")

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

def grafico_cg_at(sequencia): 
    plt.close()
    #rotulos
    percentuais = [calcular_gc(sequencia), calcular_at(sequencia)]
    pares = ["GC", "AT"]

    #código do gráfico
    plt.pie(percentuais, labels = pares, autopct = '%1.1f%%')
    plt.title("Conteúdo GC vs AT")
    plt.show()
    
def reconhece_codons(sequencia):
    stop_codons = ['TAA', 'TAG', 'TGA']
    traduzidos = {}
    for i in range(len(sequencia) - 2):
        if sequencia[i:i+3] == 'ATG':
            codons = []
            for j in range(i, len(sequencia) - 2, 3):
                trinca = sequencia[j:j+3]
                codons.append(trinca)
                if trinca in stop_codons:
                    traduzidos[i+1] = codons
                    break


    return traduzidos