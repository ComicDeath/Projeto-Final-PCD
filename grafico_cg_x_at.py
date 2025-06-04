sequencia_de_bases = "ATGCGTACGTTAGCGTACGATCGATCGTAGCTAGCTAGCGTACGATCGTAGCTAGCTAGCGTACGATCGTAGCTAGCTAGCGTACGATCGTAGCTAGCTAGCGTACGATCGTAGCTAGCTAGCGTACGATCGTAGCTAGCTAGCGTACGATCGTAGCTAGCTAGCGTACGATCGTAGCTAGCTAGCGTACGATCGTAGCTAGCTAGC"

from contagem_de_bases import calcular_gc, calcular_at

import matplotlib.pyplot as plt

#rótulos
percentuais = [calcular_gc(sequencia_de_bases), calcular_at(sequencia_de_bases)]
pares = ["GC", "AT"]

#código do gráfico
plt.pie(percentuais, labels = pares, autopct = '%1.1f%%')
plt.title("Conteúdo GC vs AT")
plt.show()