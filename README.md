# Projeto de Web Scraping e Processamento de PDFs

Este projeto tem como objetivo realizar o **web scraping** em um site institucional, baixar arquivos PDF específicos, processá-los para extrair dados relevantes e salvar essas informações em um formato estruturado. O projeto também inclui funcionalidades para compactar os arquivos processados e gerar relatórios a partir dos dados extraídos.

## Funcionalidades

- **Download de PDFs**: O projeto realiza o download de documentos em formato PDF de URLs específicas.
- **Processamento de PDFs**: A partir dos arquivos PDF baixados, o projeto extrai dados estruturados, como tabelas e informações relevantes, utilizando bibliotecas especializadas.
- **Exportação para CSV**: Os dados extraídos dos PDFs são salvos em arquivos CSV para facilitar a análise e manipulação dos dados.
- **Compactação de Arquivos**: Todos os arquivos gerados (PDFs e CSVs) são compactados em um arquivo ZIP para facilitar o armazenamento e o envio.

## Estrutura do Projeto

- **`/output`**: Contém os arquivos gerados durante o processo (PDFs, CSVs, arquivos compactados).
- **`/scraping`**: Scripts responsáveis pelo download dos PDFs, processamento dos documentos e extração de tabelas.
- **`/pdfs`**: Diretório utilizado para armazenar os PDFs baixados.
- **`main.py`**: O script principal que executa as tarefas de download, processamento e exportação dos dados.
- **`requirements.txt`**: Arquivo de dependências, utilizado para instalar as bibliotecas necessárias para o funcionamento do projeto.

## Tecnologias Utilizadas

- **Python**: A linguagem principal utilizada para desenvolver o projeto.
- **Bibliotecas**:
  - `requests`: Para realizar o download dos arquivos PDF.
  - `pdfplumber`: Para processar e extrair dados das tabelas nos arquivos PDF.
  - `pandas`: Para manipulação dos dados extraídos e exportação para o formato CSV.
  - `zipfile`: Para compactação dos arquivos em formato ZIP.

## Como Executar

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/usuario/MeuProjetoPY.git
   cd MeuProjetoPY

   

