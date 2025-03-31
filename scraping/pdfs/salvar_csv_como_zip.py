import zipfile
import os
import pandas as pd

def salvar_csv_como_zip(df, output_csv, zip_filename):
    # Salvar o CSV
    df.to_csv(output_csv, index=False)
    print(f"Arquivo CSV salvo em: {output_csv}")

    # Compactando o CSV em um arquivo ZIP
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(output_csv, os.path.basename(output_csv))
    print(f"Arquivo ZIP salvo em: {zip_filename}")

    # Remover o CSV após compactação
    os.remove(output_csv)
    print(f"Arquivo CSV removido após compactação.")
