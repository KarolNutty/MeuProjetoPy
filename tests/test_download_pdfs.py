import os
import pytest
from scraping.pdfs.download_pdfs import download_pdf  # Corrigido para o caminho correto

def test_download_pdfs():
    # Diretório onde os PDFs devem estar
    pdfs_dir = os.path.join('E:', 'MeuProjetoPY', 'pdfs')

    # Caminhos completos dos arquivos PDF
    pdf_path_1 = os.path.join(pdfs_dir, 'Anexo_I.pdf')
    pdf_path_2 = os.path.join(pdfs_dir, 'Anexo_II.pdf')

    # URLs para os PDFs (substitua pelas URLs reais)
    url_pdf_1 = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf'
    url_pdf_2 = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf'

    # Verifica se o diretório pdfs existe, se não, cria
    if not os.path.exists(pdfs_dir):
        os.makedirs(pdfs_dir)
        print(f"Diretório {pdfs_dir} criado.")

    # Baixar os arquivos PDF se eles não existirem
    if not os.path.exists(pdf_path_1):
        print(f"Baixando {pdf_path_1}...")
        download_pdf(url_pdf_1, pdf_path_1)

    if not os.path.exists(pdf_path_2):
        print(f"Baixando {pdf_path_2}...")
        download_pdf(url_pdf_2, pdf_path_2)

    # Verifica se os arquivos PDF existem no diretório
    assert os.path.exists(pdf_path_1), f"{pdf_path_1} não foi encontrado"
    assert os.path.exists(pdf_path_2), f"{pdf_path_2} não foi encontrado"






