import os
import requests


def download_pdf(url, destination):
    """Baixa um PDF da URL e salva no destino fornecido."""
    # Verifica se a pasta de destino existe, senão, cria
    folder = os.path.dirname(destination)
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"Pasta '{folder}' criada.")

    # Faz a requisição para o link
    response = requests.get(url)

    # Verifica se o tipo de conteúdo é PDF
    if 'application/pdf' in response.headers.get('Content-Type', ''):
        with open(destination, 'wb') as file:
            file.write(response.content)
        print(f"PDF {destination} baixado com sucesso!")
    else:
        print(f"A URL {url} não retornou um PDF válido, mas sim {response.headers.get('Content-Type')}")




