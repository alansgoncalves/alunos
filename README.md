# Importação de dados csv para o Solr" 📊

Este script Python lê um arquivo CSV contendo dados do aluno, realiza a limpeza de dados usando a biblioteca pandas e insere os dados limpos no Apache Solr. O objetivo é fornecer um exemplo simples de importação de dados para o Solr usando Python.

# Requisitos:
- Python 3.x
- pandas
- pysolr
- Apache Solr

# Configuração core Solr
1. Clone o repositório:
   ```bash
   git clone https://github.com/alansgoncalves/alunos.git
   cd alunos

2. Acesse o diretório configsets do seu solr:
   ```bash
   cd server/solr/configsets

3. Crie um novo diretório dentro de configsets
   ```bash
   configsets mkdir search_alunos

4. Copie as definições de configuração do diretório _default
   ```bash
   configsets cp -r _default/. search_alunos

5. Acesse o diretório conf de search_alunos
   ```bash
   configsets cd search_alunos/conf

6. Rode o comando a seguir para criar o core do Solr usando o conjunto de configurações search_alunos que acabamos de criar
   ```bash
   conf curl -X GET 'http://localhost:8983/solr/admin/cores?action=create&name=search_alunos&instanceDir=configsets/search_alunos'

   
