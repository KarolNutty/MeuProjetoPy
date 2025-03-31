import os
import pandas as pd

from scraping.pdfs.extract_table_from_pdf import extract_table_from_pdf


def test_csv_data_processing():
    # Caminho do arquivo CSV
    csv_output = 'pdfs/output/tabela_extraida.csv'  # Usando a pasta 'pdfs/output' como exemplo

    # Verifica se o diretório de saída existe, se não, cria
    if not os.path.exists(os.path.dirname(csv_output)):
        os.makedirs(os.path.dirname(csv_output))

    # Caminho do arquivo PDF (Dentro do diretório 'pdfs')
    pdf_path = 'pdfs/Anexo_I.pdf'

    # Chama a função que gera o CSV (presumindo que essa função cria o arquivo CSV)
    extract_table_from_pdf(pdf_path, csv_output)

    # Verifica se o CSV foi criado
    assert os.path.exists(csv_output), f"O arquivo CSV {csv_output} não foi criado."

    # Verifica se o CSV contém dados (não está vazio)
    df = pd.read_csv(csv_output)
    assert not df.empty, f"O arquivo CSV {csv_output} está vazio."

    # Verifica se o CSV possui pelo menos uma coluna (substitua pelo nome da coluna real que você espera)
    assert 'Procedimento' in df.columns, f"A coluna 'Procedimento' não foi encontrada no CSV."


