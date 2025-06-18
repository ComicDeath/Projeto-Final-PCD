sequencia_de_bases = """ATGAGTATTCAACATTTCCGTGTCGCCCTTATTCCCTTTTTTGCGGCATTTTGCCTTCCTGTTTTTGCTCACCCAGAACGCTGGTGAAAGTAAAAGATGCTGAAGATCAGTTGGGTGCACGAGTGGGTTACATCGAACTGGATCTCAACAGCGGTAAGATCCTTGAGAGTTTTCGCCCCGAAGTTTGCGCGGTCATGTGCGCAGCGGTCGGGCTGAACAGCTTGCTGGTGAAAAGTTTGAGGGGACGATGTCACTGGCTGAGCACAAACGGTGTAACGGGATCTTCACCTAGATCCTTTTTGATAATCTCATGACCAAAATCCGTTTGATTTTGATGGTGGTGGCGGTCTATGGGTAAAGTTGCCGTGTTGCTGGCGGCGGTGTTTTTCCTGTTTTTGCTCACCCAGAAACGCTGGTGAAAGTATTGACCGTACGATCGTAGCTAGCTAGATGAGGGAAGCGGTTGGGAGATGAGGATCGTTTCGCATGATTGAACAAGATGGATTGCACGCAGGTTCTCCGGCCGCTTGGGTGGAGAGGCTATTCGGCTATGACTGGGCACAACAGACAATCGGCTGCTCTGATGCCGCCGTGTTCCGGCTGTCAGCGCAGGGGCGCCCGGTTCTTTTTGTCAAGACCGACCTGTCCGGTGCCCTGAATGAACTGCAGGACGAGGCAGCGCGGCTATCGTGGCTGGCCACGACGGGCGTTCCTTGCGCAGCTGTGCTCGACGTTGTCACTGAAGCGGGAAGGGACTGGCTGCTATTGGGCGAAGTGCCGGGGCAGGATCTCCTGTCATCTCACCTTGCTCCTGCCGAGAAAGTATCCATCATGGCTGATGCAATGCGGCGGCGAGTTTGAGGATCGTTTCGCATGATTGAACAAGATGGATTGCACGCAGGTTGCTAGCTAGCTAGCTAGATGAGAAAAATCGAAGAAGGTAAACTGGCTCGGATTGGCGAAGTTAGTAGCGGTCACAGCTTGTCTGGAAGAAGTCCATTGAAATCGAAGTGGGTGGTAGCGAAGTTTGTTCAACCCGAATGAGATTGATGTTGATGATTTTATTTTCACTGGCGTTAAGACGTTTTCTTGGGCGCTATGCCCGCAGTAAATTGCTGGCAGCAAAATCAATGCAAGTAGCTGGAATGCTGATGTTGGGTTGGTGAAGCGGTGACGAGGTGATGTATCAGGGGTATCGTCAGGTGATGATTTGACGTCACGGTTGGAAGTGGAAATTGCTCTTGTGGTCTGGTAGTAGTTTGTAATAGTTGTGCGCAGCCTGAAGCGAA"""

#Importa da bilblioteca os genes de resistencia
from bibliotecas import *

#Função para identificar os genes de resistencia e sua posição no genoma
def identifica_genes_resistencia(sequencia_de_bases):

    #O replace é para garantir que não terão espaos atrapalhando
    sequencia_de_bases = sequencia_de_bases.replace('\n', '')
    resultados = []

    #O for navega pelos itens do gene_resistencia da biblioteca
    for nome_gene, sequencia_gene in genes_resistencia.items():
        posicao = sequencia_de_bases.find(sequencia_gene)

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
            posicao = sequencia_de_bases.find(sequencia_gene, posicao + 1)

    # Testa se a lista resultados não está vazia indicando que um gene foi encontrado.
    if resultados:
        return resultados
    
    #Caso nenhum gene seja encontrado retorna a frase abaixo.
    else:
        return "No seu plasmídio não há genes de resistência"

# Testando
resultados = identifica_genes_resistencia(sequencia_de_bases)
for r in resultados:
    print(f"Gene {r['gene']} encontrado na posição {r['posicao']}, tamanho: {r['tamanho']}, antibiótico: {r['antibiotico']}")

# Nesse código precisei de ajuda da IA Perplexity para corrigir alguns posntos, como para ele navegar em todo código antes de retonar para o caso de ter mais de um gene e ele também sugeriu o uso de replace('\n', '') pois os espaços estavam atrapalhando a dentificação, foi feita essa alteração na biblioteca também pela mesma sugestão.