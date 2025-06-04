def capturaDados(entrada, resultado): 
    sequencia = entrada.get().strip().upper()
    with open("assets/sequencia.txt", "w") as f:
        f.write(sequencia)
    resultado.config(text=f"Sequência armazenada: {sequencia}")

def Temperatura_Melting(sequencia):
    melting = 64.9 + 41 * (gc - 16.4) / tamanho_total
    return melting



