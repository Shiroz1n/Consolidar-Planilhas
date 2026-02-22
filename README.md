Consolidador de Planilhas Excel com Python
Este script automatiza a união de múltiplos arquivos Excel (.xlsx e .xls) em um único arquivo consolidado, aplicando tratamentos de dados e gerando um relatório estatístico básico ao final do processo.

O que o projeto faz?
Varredura Automática: Busca todos os arquivos de uma pasta.

Consolidação Inteligente: Une as planilhas uma abaixo da outra, mesmo que os nomes das colunas variem (resetando os índices).

Data Lineage: Adiciona colunas extras para indicar de qual arquivo o dado veio e quando ele foi processado.

Análise de Dados: Identifica valores nulos e calcula métricas financeiras (Soma, Média, Máximo e Mínimo) automaticamente.

Como rodar o script
Instale o Pandas:
pip install pandas openpyxl

No código, altere o caminho da variável pasta_vendas para o local onde estão seus arquivos.

Execute o script