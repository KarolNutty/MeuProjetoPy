import zipfile
import os

def compactar_arquivos(pdf_paths, zip_filename):
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for pdf in pdf_paths:
            zipf.write(pdf, os.path.basename(pdf))
            print(f"Arquivo {pdf} adicionado ao ZIP.")
    print(f"Arquivo ZIP criado com sucesso: {zip_filename}")
