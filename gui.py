import tkinter as tk
from main import capturaDados, carregaArquivo, grafico_cg_at, enzimas_de_restricao, identifica_genes_resistencia, temperatura_melting

janela = tk.Tk()
janela.title("Plasmid Computer Decoder")
janela.geometry("500x300")

imagem_pasta = tk.PhotoImage(file="assets/folder_true.png")
imagem_pasta = imagem_pasta.subsample(14, 14)

frameCnt = 9 
frames = [tk.PhotoImage(file="assets/12.gif", format=f"gif -index {i}") for i in range(frameCnt)]

def gif(label, ind=0):
    frame = frames[ind]
    ind = (ind + 1) % frameCnt
    label.config(image=frame)
    janela.after(12, gif, label, ind)

linha = tk.Frame(janela)
linha.pack(pady=10)

label_gif_esquerda = tk.Label(linha)
label_gif_esquerda.pack(side=tk.LEFT, padx=5)
gif(label_gif_esquerda)

label_texto = tk.Label(linha, text="Digite a sequência de DNA (ex: ATCGTAGC):", font=("Arial", 12))
label_texto.pack(side=tk.LEFT, padx=10)

label_gif_direita = tk.Label(linha)
label_gif_direita.pack(side=tk.LEFT, padx=5)
gif(label_gif_direita)

frame_da_entrada = tk.Frame(janela)
frame_da_entrada.pack(pady=5)

entrada = tk.Entry(frame_da_entrada, font=("Arial", 14), justify="center", width=30)
entrada.pack(side=tk.LEFT)

icone_pasta = tk.Button(frame_da_entrada, image=imagem_pasta, command=lambda: carregaArquivo(entrada))
icone_pasta.pack(side=tk.LEFT, padx=5)

#PRIMEIRA LINHA DE BOTOES

linha_botoes_1 = tk.Frame(janela)
linha_botoes_1.pack(pady=10)

botao_graficos = tk.Button(linha_botoes_1, text="Gráfico de bases GC x AT", command=lambda: grafico_cg_at(entrada, resultado))
botao_graficos.pack(side=tk.LEFT, padx=10, pady=10)

botao_enzima_de_restrição = tk.Button(linha_botoes_1, text="Enzima de restrição", command=lambda: enzimas_de_restricao(entrada, resultado) )
botao_enzima_de_restrição.pack(side=tk.RIGHT, padx=10, pady=10)

linha_botoes_2 = tk.Frame(janela)
linha_botoes_2.pack(pady=10)

botao_gene_de_resistencia = tk.Button(linha_botoes_2, text="Gene de resistência", command=lambda: identifica_genes_resistencia(entrada, resultado))
botao_gene_de_resistencia.pack(side=tk.LEFT, padx=10, pady=10)

botao_temperatura_melting = tk.Button(linha_botoes_2, text="Temperatura de melting", command=lambda: temperatura_melting(entrada.get(), resultado))
botao_temperatura_melting.pack(side=tk.LEFT, padx=10, pady=10)

resultado = tk.Label(janela, text="", font=("Arial", 12))
resultado.pack(pady=20)

janela.mainloop()