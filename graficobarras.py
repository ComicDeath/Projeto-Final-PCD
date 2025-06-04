import matplotlib.pyplot as plt
from contagem_de_bases import conta_A, conta_G, conta_T, conta_C

nome_das_bases = ["Adenina", "Guanina", "Timina", "Citosina"]
lista_de_quantidades = [conta_A, conta_G, conta_T, conta_C]

plt.figure(dpi=240)

plt.bar(nome_das_bases, lista_de_quantidades, width=0.8)

plt.title('Quantidade de cada base')
plt.xlabel('Bases nitrogenadas')
plt.ylabel('Número de bases')

plt.show()