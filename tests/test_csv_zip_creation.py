import os
import zipfile
import pytest
import pandas as pd  # Certifique-se de importar pandas

from scraping.pdfs.salvar_csv_como_zip import salvar_csv_como_zip


def test_csv_zip_creation():
    # Caminhos dos arquivos
    output_dir = 'pdfs/output'  # Diretório onde os arquivos serão salvos
    csv_output = os.path.join(output_dir, 'tabela_extraida.csv')
    zip_output = os.path.join(output_dir, 'Teste_SeuNome.zip')

    # Verifica se o diretório de saída existe, se não, cria
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Gera o CSV e compacta em ZIP
    # Supondo que você tenha algum mecanismo para gerar o CSV
    # salvar_csv_como_zip(pd.read_csv(csv_output), csv_output, zip_output)

    # Geração do CSV de exemplo (você pode comentar ou ajustar com a função real)
    df = pd.DataFrame({'Coluna1': [1, 2, 3], 'Coluna2': ['A', 'B', 'C']})
    df.to_csv(csv_output, index=False)  # Gerar o CSV de exemplo

    # Função de compactação do CSV em ZIP
    salvar_csv_como_zip(pd.read_csv(csv_output), csv_output, zip_output)

    # Verifica se o arquivo ZIP foi criado
    assert os.path.exists(zip_output), f"O arquivo ZIP {zip_output} não foi criado."

    # Verifica se o ZIP contém o CSV esperado
    with zipfile.ZipFile(zip_output, 'r') as zip_file:
        zip_file.extractall(output_dir)
        assert os.path.exists(csv_output), f"O arquivo {csv_output} não foi encontrado no ZIP."

