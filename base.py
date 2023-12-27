import pandas as pd
import pysolr
import logging

# Configuração de menasagens de log
logging.basicConfig(filename='import_to_solr.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

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
    
    # Log para limpeza de dados
    logging.info('Limpeza de dados concluída com sucesso!')

    return df

# Função para inserir os dados CSV para core do Solr
def insert_into_solr(data):
    solr_url = 'http://localhost:8983/solr'  # Variável que armazena URL de acesso ao Solr
    solr_core = 'search_alunos'  # Variável que armazena o nome do core Solr

    # Variável que utiliza a biblioteca pysolr para fazer conexão com o Solr
    solr = pysolr.Solr(f'{solr_url}/{solr_core}', always_commit=True)

    # For loop para iterar cada linha do arquivo e inserir no core do Solr
    for index, row in data.iterrows():
        # Converte os dados da coluna 'Data de Nascimento' de Timestamp para string
        birth_date_str = str(row['Data de Nascimento'])

        # Mapeia os campos do aquivo csv para os campos correspondentes no schema do Solr
        solr_data = {
            'name': row['Nome'],
            'age': row['Idade'],
            'grade': row['Série'],
            'average_score': row['Nota Média'],
            'address': row['Endereço'],
            'father_name': row['Nome do Pai'],
            'mother_name': row['Nome da Mãe'],
            'birth': birth_date_str,
        }

        # Insere os dados no Solr
        solr.add([solr_data])
        
        # Log de progresso para cada registro inserido no Solr
        logging.info(f'Dados para {row["Nome"]} inserido no Solr')

# Condição que garante que as funções necessárias sejam chamadas na ordem correta:
# Leitura do arquivo CSV, limpeza dos dados e inserção dos dados limpos no Solr
# Só será executado se o script estiver sendo executado diretamente.
if __name__ == '__main__':
    # Variável que armazena o arquivo aluno.csv
    csv_file = './csv/aluno.csv'
    
    # Log de início de execução
    logging.info('Script de execução iniciado!')

    # Variável que aplica a função read_and_clean_csv Read ao arquivo csv
    cleaned_data = read_and_clean_csv(csv_file)

    # Chama a função insert_into_solr para inserir os dados limpos no Solr
    insert_into_solr(cleaned_data)
    
    # Log de execução completa
    logging.info('Script de execução completo!')