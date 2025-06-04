def analises_basicas(sequencia_de_bases):
    
    conta_A = sequencia_de_bases.count("A")
    conta_C = sequencia_de_bases.count("C")
    conta_G = sequencia_de_bases.count("G")
    conta_T = sequencia_de_bases.count("T")

    tamanho_total = sequencia_de_bases.count("A") + sequencia_de_bases.count("G") + sequencia_de_bases.count("C") + sequencia_de_bases.count("T")
    return tamanho_total

def conta_A(sequencia_de_bases):
    
    conta_A = sequencia_de_bases.count("A")
    return conta_A

def conta_C(sequencia_de_bases):
    
    conta_C = sequencia_de_bases.count("C")
    return conta_C

def conta_G(sequencia_de_bases):
    
    conta_G = sequencia_de_bases.count("G")
    return conta_G

def conta_T(sequencia_de_bases):
    
    conta_T = sequencia_de_bases.count("T")
    return conta_T

def calcular_gc(sequencia_de_bases):
    gc = sequencia_de_bases.count("G") + sequencia_de_bases.count("C")
    return gc / len(sequencia_de_bases) * 100

def calcular_at(sequencia_de_bases):
    at = sequencia_de_bases.count("A") + sequencia_de_bases.count("T")
    return at / len(sequencia_de_bases) * 100

sequencia_de_bases = "ATGCGTACGTTAGCGTACGATCGATCGTAGCTAGCTAGCGTACGATCGTAGCTAGCTAGCGTACGATCGTAGCTAGCTAGCGTACGATCGTAGCTAGCTAGCGTACGATCGTAGCTAGCTAGCGTACGATCGTAGCTAGCTAGCGTACGATCGTAGCTAGCTAGCGTACGATCGTAGCTAGCTAGCGTACGATCGTAGCTAGCTAGC"

print(analises_basicas(sequencia_de_bases))
print(calcular_gc(sequencia_de_bases))
print(calcular_at(sequencia_de_bases))
print(conta_A(sequencia_de_bases))
print(conta_C(sequencia_de_bases))
print(conta_G(sequencia_de_bases))
print(conta_T(sequencia_de_bases))