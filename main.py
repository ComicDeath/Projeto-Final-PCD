def capturaDados(entrada, resultado): 
    sequencia = entrada.get().strip().upper()
    with open("assets/sequencia.txt", "w") as f:
        f.write(sequencia)
    resultado.config(text=f"Sequência armazenada: {sequencia}")

    total = len(sequencia)

def calcular_gc(sequencia):
    gc = sequencia_de_bases.count("G") + sequencia_de_bases.count("C")
    return gc

def Temperatura_Melting(sequencia):
    melting = 64.9 + 41 * (gc - 16.4) / total
    return melting
