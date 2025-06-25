![ILUM, CNPEM, MINISTÉRIO DA EDUCAÇÃO](https://github.com/ComicDeath/Projeto-Final-PCD/blob/main/assets/ilum_colorida.png)

<h1 align="center"> PCD - Plasmid Computer Decoder </h1>

O projeto PCD (Plasmid Computer Decoder) foi desenvolvido como projeto final da matéria Práticas em Ciências de Dados por estudantes da Ilum - Escola de Ciências. O PCD recebe uma sequência de DNA ou RNA plasmidial inserida pelo usuário ou carregada via arquivo .txt ou .FASTA. Com essa sequência, pode-se exercer as seguintes funções:
### `Temperatura de melting`
Retorna o valor da temperatura de melting em grau Celcius com precisão de uma casa decimal. 
### `Enzimas de restrição`
Retorna um arquivo .txt com o nome e a frequência das enzimas de restrição identificadas.
### `Gráfico dos pares AT e CG`
Retorna um gráfico de seção com a porcentagem dos pares AT e CG presentes no plasmídeo.
### `Genes de resistência`
Retorna um arquivo .txt com o nome dos genes de resistência identificados, a posição, o tamanho e o antibiótico correspondente.
### `Identificação de proteínas`
Retorna um arquivo .txt com os aminoácidos codificados pela sequência.

# Instalação
Para executar o projeto, deve-se clonar esse repositório em sua máquina e abri-lo em uma IDE compatível com Python. Depois, basta abrir e executar o arquivo gui.py para abrir a interface pronta para uso.

# Construído com
- **Python** - linguagem de programação;
- **TKinter** - biblioteca para criação da GUI;
- **MatPlotLib** - biblioteca para criação e visualização de gráficos;

# Informações adicionais
Para mais informações sobre as funções imbutidas e usos do software, consulte o pdf anexado `PCD - Atividade Final`.

# Integrantes
O projeto foi desenvolvido por um grupo de estudantes cursando o primeiro semestre do bacharelado em ciência e tecnologia oferecido pela Ilum Escola de Ciências - instituição de ensino superior do CNPEM.
- [**Brenda Laube Abrunhosa**](https://github.com/blabrunhosa)
  * Validação da sequência;
  * Suporte para RNA;
  * Função das enzimas de restrição;
  * Gráfico de barras;
  * Contribuiu na montagem do README, do relatório e dos slides.
- [**Matheus Nascimento Cunha**](https://github.com/mncunha)
  * Função da Temperatura de Melting;
  * Função da leitura de transcritos e a tradução deles;
  * Criação do dicionário de genes de resistência;
  * Criação do grafo do código genético;
  * Criação do Toy Model para a experimentação;
  * Auxiliou os demais membros com o conteúdo teórico em biologia.
- [**Sarah Santos Silva**](https://github.com/SarahSantosSilva)
  * Contagem de bases;
  * Gráfico de porcentagem de at X gc;
  * Função de gene de restrição;
  * Além disso ajudou o grupo com a organização dos slides e do relatório.
- [**João Henrique de Lima Gasquez**](https://github.com/ComicDeath)
  * Construção da interface gráfica;
  * Configuração dos arquivos de saída;
  * Formatação das funções para integração com a interface;
  * Auxiliou os demais membros na utilização do VSCode e do GitHub;
  * Auxiliou os demais membros em erros e dúvidas no código;
  * Contribuiu na montagem do README, do relatório e dos slides.
  
# Docentes
A matéria Práticas em Ciências de Dados foi ministrada por:
- **Profº Dr. Leandro Nascimento Lemos**
- **Profº Dr. Daniel Roberto Cassar**
- **Profº Dr. James Moraes de Almeida**

# Licença
Distribuído sob a licença GNU General Public License 3.0, cheque `LICENSE` para mais informações.

## Referências para a construção do README
 ROCKETSEAT. **Como fazer um bom README.** Disponível em: https://blog.rocketseat.com.br/como-fazer-um-bom-readme/. Acesso em: 22 de jun. 2025.

![ILUM, CNPEM, MINISTÉRIO DA EDUCAÇÃO](https://github.com/ComicDeath/Projeto-Final-PCD/blob/main/assets/ilum.png)
