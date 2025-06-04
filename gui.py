import tkinter as tk
from main import capturaDados

janela = tk.Tk()
janela.title("Plasmid Computer Decoder")
janela.geometry("500x350")

frameCnt = 9 
frames = [tk.PhotoImage(file="assets/12.gif", format=f"gif -index {i}") for i in range(frameCnt)]

def gif(label, ind=0):
    frame = frames[ind]
    ind = (ind + 1) % frameCnt
    label.config(image=frame)
    label.image = frame
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

entrada = tk.Entry(janela, font=("Arial", 14), justify="center")
entrada.pack(pady=5)

botao = tk.Button(janela, text="Iniciar", command=lambda: capturaDados(entrada, resultado))
botao.pack(pady=5)

resultado = tk.Label(janela, text="", font=("Arial", 12))
resultado.pack(pady=20)

janela.mainloop()