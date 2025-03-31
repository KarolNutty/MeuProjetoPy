import camelot
import pandas as pd


def extract_table_from_pdf(pdf_path, csv_output_path):
    # Usando Camelot para extrair tabelas do PDF
    tables = camelot.read_pdf(pdf_path, pages='1',
                              flavor='stream')  # 'stream' é bom para PDFs com tabelas de texto contínuo

    if tables:
        # Convertendo a primeira tabela extraída para DataFrame
        df = tables[0].df

        # Salvando a tabela extraída como CSV
        df.to_csv(csv_output_path, index=False, header=False)
        print(f"CSV criado em: {csv_output_path}")
    else:
        print("Nenhuma tabela encontrada no PDF.")
