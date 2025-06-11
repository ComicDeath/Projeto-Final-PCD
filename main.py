import tkinter as tk
import matplotlib.pyplot as plt
import os
from contagem_de_bases import calcular_gc, calcular_at
from tkinter import filedialog
from bibliotecas import enzimas, codigo_genetico, antibioticos, genes_resistencia

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
    if len(sequencia_crua) == 0:
        valido = False
    else:
        for letra in sequencia_crua:
            if letra not in bases_esperadas and letra not in bases_rna:
                valido = False
                break
    
    if "T" in sequencia_crua and "U" in sequencia_crua:
        valido = False

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
        with open("assets/sequencia.txt", "w") as f:
            f.write("")
            saida = "Sequência inválida."
            resultado.config(text=saida)
            sequenciaVar("assets/sequencia.txt")
            return "Erro"
        
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

def Temperatura_Melting(sequencia):
    gc = calcular_gc(sequencia)
    total = len(sequencia)
    melting = 64.9 + 41 * (gc- 16.4) / total
    return melting

def enzimas_de_restricao(entrada, resultado):
    capturaDados(entrada, resultado)
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

    with open("assets\\enzima_de_restricao.txt", "w") as f:
            f.write(enzimas_restricao_tabela)
    os.startfile("assets\\enzima_de_restricao.txt")

def grafico_cg_at(entrada, resultado): 
    capturaDados(entrada, resultado)
    if capturaDados(entrada, resultado) != "Erro":
        plt.close()
        
        #rotulos
        percentuais = [calcular_gc(sequencia), calcular_at(sequencia)]
        pares = ["GC", "AT"]

        #código do gráfico
        plt.pie(percentuais, labels = pares, autopct = '%1.1f%%')
        plt.title("Conteúdo GC vs AT")
        plt.show()

def reconhece_proteinas(sequencia):
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

    # Traduzir códons para aminoácidos
    proteinas = {}
    for posicao, lista_codons in traduzidos.items():
        prot = []
        for trinca in lista_codons:
            for aa, codons in codigo_genetico.items():
                if trinca in codons:
                    if aa == 'STOP':
                        break
                    prot.append(aa)
                    break
        proteinas[posicao] = prot

    return proteinas

#Função para identificar os genes de resistencia e sua posição no genoma
def identifica_genes_resistencia(entrada, resultado):
    capturaDados(entrada, resultado)
    #O replace é para garantir que não terão espaos atrapalhando
    resultados = []

    #O for navega pelos itens do gene_resistencia da biblioteca
    for nome_gene, sequencia_gene in genes_resistencia.items():
        posicao = sequencia.find(sequencia_gene)

        #O While para ele continuar identificando gene possíveis
        while posicao != -1:
            tamanho = len(sequencia_gene)
            antibiotico = antibioticos[nome_gene]
            resultados.append({
                'gene': nome_gene,
                'posicao': posicao,
                'tamanho': tamanho,
                'antibiotico': antibiotico
            })

            #Posição atualiza a variável para buscar o próximo gene de resistencia
            posicao = sequencia.find(sequencia_gene, posicao + 1)

    # Testa se a lista resultados não está vazia indicando que um gene foi encontrado.
    if resultados:
        with open("assets\\gene_de_resistencia.txt", "w") as f:
            for r in resultados:
                f.write(f"Gene {r['gene']} encontrado na posição {r['posicao']}, tamanho do gene de resistência: {r['tamanho']}, antibiótico: {r['antibiotico']} \n")
        os.startfile("assets\\gene_de_resistencia.txt")
    
    #Caso nenhum gene seja encontrado retorna a frase abaixo.
    else:
        resultado.config(text="No seu plasmídio não há genes de resistência")
    
