# Importação de dados csv para o Solr" 📊

Este script Python lê um arquivo CSV contendo dados do aluno, realiza a limpeza de dados usando a biblioteca pandas e insere os dados limpos no Apache Solr. O objetivo é fornecer um exemplo simples de importação de dados para o Solr usando Python.

# Requisitos:
- Python 3.x
- pandas
- pysolr
- Apache Solr


# Configuração core Solr
1. Acesse o diretório configsets do seu solr:
   ```bash
   cd server/solr/configsets

2. Crie um novo diretório dentro de configsets
   ```bash
   configsets mkdir search_alunos

3. Copie as definições de configuração do diretório _default
   ```bash
   configsets cp -r _default/. search_alunos

4. Acesse o diretório conf de search_alunos
   ```bash
   configsets cd search_alunos/conf

5. Rode o comando a seguir para criar o core do Solr usando o conjunto de configurações search_alunos que acabamos de criar
   ```bash
   conf curl -X GET 'http://localhost:8983/solr/admin/cores?action=create&name=search_alunos&instanceDir=configsets/search_alunos'

6. Clone o repositório
   ```bash
   git clone https://github.com/alansgoncalves/alunos.git
   cd alunos


# Leitura e limpeza de dados

Para realizar a leitura e limpeza dos dados do arquivo aluno.csv, utilizamos a biblioteca pandas:
```Python
import pandas as pd

# Função para leitura e limpeza dos dados do arquivo CSV
def read_and_clean_csv(csv_file):
    # Realiza a leitura do arquivo utilizando a biblioteca pandas
    df = pd.read_csv(csv_file)

    # Elimina linhas com valores ausentes
    df = df.dropna()

    # Converte os dados das colunas 'Idade' e 'Nota Média' para tipo numérico
    df['Idade'] = pd.to_numeric(df['Idade'], errors='coerce')
    df['Série'] = pd.to_numeric(df['Série'], errors='coerce')
    df['Nota Média'] = pd.to_numeric(df['Nota Média'], errors='coerce')

    # Coverte os dados da coluna 'Data de Nascimento' para tipo datetime
    df['Data de Nascimento'] = pd.to_datetime(df['Data de Nascimento'], errors='coerce')

    return df
```

