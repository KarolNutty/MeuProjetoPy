import zipfile
import pandas as pd
import os

from scraping.pdfs.download_pdfs import download_pdf
from scraping.pdfs.extract_table_from_pdf import extract_table_from_pdf
from scraping.pdfs.get_pdf_links_from_page import get_pdf_links_from_page
from scraping.pdfs.salvar_csv_como_zip import salvar_csv_como_zip
from scraping.pdfs.compactar_arquivos import compactar_arquivos


def iniciar_processos():
    # URL da página com os links dos PDFs
    page_url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

    # Obter os links dos PDFs da página
    pdf_links = get_pdf_links_from_page(page_url)

    if not pdf_links:
        print("Não foi possível encontrar links para os PDFs.")
        return

    # Caminhos dos arquivos PDF
    pdf_path_1 = 'output/pdfs/Anexo_I.pdf'
    pdf_path_2 = 'output/pdfs/Anexo_II.pdf'
    zip_pdf_output = 'output/Anexos.zip'
    csv_output = 'output/tabela_extraida.csv'
    zip_csv_output = 'output/Teste_seu_nome.zip'

    # Baixar os PDFs
    print("Iniciando o download dos arquivos PDF...")
    download_pdf(pdf_links[0], pdf_path_1)  # Baixa o primeiro PDF
    download_pdf(pdf_links[1], pdf_path_2)  # Baixa o segundo PDF (ajuste conforme o número de PDFs)

    # Compactar PDFs
    print("Compactando PDFs...")
    compactar_arquivos([pdf_path_1, pdf_path_2], zip_pdf_output)

    # Simulando a extração da tabela e salvando como CSV
    print("Extraindo a tabela do PDF...")
    extract_table_from_pdf(pdf_path_1, csv_output)

    # Compactar o CSV em ZIP
    df = pd.read_csv(csv_output)  # Lê o CSV
    salvar_csv_como_zip(df, csv_output, zip_csv_output)


if __name__ == '__main__':
    iniciar_processos()


