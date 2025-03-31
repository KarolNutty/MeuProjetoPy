import os
import pandas as pd
import pytest

from scraping.pdfs.extract_table_from_pdf import extract_table_from_pdf


def test_pdf_to_csv_conversion():
    # Diretórios onde os arquivos são armazenados
    pdfs_dir = 'pdfs'
    output_dir = 'output'

    # Caminhos dos arquivos
    pdf_path = os.path.join(pdfs_dir, 'Anexo_I.pdf')
    csv_output = os.path.join(output_dir, 'tabela_extraida.csv')

    # Verifica se o diretório de saída existe, se não, cria
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Chama a função que extrai os dados do PDF e gera o CSV
    extract_table_from_pdf(pdf_path, csv_output)

    # Verifica se o CSV foi criado
    assert os.path.exists(csv_output), f"O arquivo CSV {csv_output} não foi criado."

    # Verifica se o CSV contém dados (não está vazio)
    df = pd.read_csv(csv_output)
    assert not df.empty, f"O arquivo CSV {csv_output} está vazio."

    # Verifica se o CSV contém uma das colunas esperadas
    expected_columns = ['Procedimento', 'Código', 'Valor']
    for column in expected_columns:
        assert column in df.columns, f"A coluna esperada '{column}' não foi encontrada no CSV."


