def capturaDados(entrada, resultado): 
    sequencia = entrada.get().strip().upper()
    with open("assets/sequencia.txt", "w") as f:
        f.write(sequencia)
    resultado.config(text=f"Sequência armazenada: {sequencia}")