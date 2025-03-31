from bs4 import BeautifulSoup
import requests

def get_pdf_links_from_page(url):
    """Obtém os links para os arquivos PDF de uma página HTML."""
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        pdf_links = []

        # Encontrar links <a> que contêm '.pdf' no href
        for a in soup.find_all('a', href=True):
            if '.pdf' in a['href']:
                # Caso o link não seja absoluto, converte para absoluto
                full_url = a['href'] if a['href'].startswith('http') else url + a['href']
                pdf_links.append(full_url)

        return pdf_links
    else:
        print(f"Erro ao acessar a página: status code {response.status_code}")
        return []
