sequencia_de_bases = "ATGCGTACGTTAGCGTACGATCGATCGTAGCTAGCTAGCGTACGATCGTAGCTAGCTAGCGTACGATCGTAGCTAGCTAGCGTACGATCGTAGCTAGCTAGCGTACGATCGTAGCTAGCTAGCGTACGATCGTAGCTAGCTAGCGTACGATCGTAGCTAGCTAGCGTACGATCGTAGCTAGCTAGCGTACGATCGTAGCTAGCTAGC"

#Importa da bilblioteca os genes de resistencia
from bibliotecas import *

#Função para identificar os genes de resistencia
def identifica_genes_resistencia(sequencia_de_bases):
    for bases in sequencia_de_bases:
        print(bases)
#         if genes_resistencia in sequencia_de_bases:
#             genes_identificados = len(genes_resistencia)

# #posição e antibiótico
    
#     return genes_identificados

print(identifica_genes_resistencia(sequencia_de_bases))