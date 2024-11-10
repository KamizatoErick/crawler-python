# Esse script entra no site da SEFAZ e confere se está ativo a contingência ou se há agendamento

import requests
from bs4 import BeautifulSoup

# URL alvo
url = 'https://www.nfe.fazenda.gov.br/portal/principal.aspx'

# Envia a requisição HTTP e obtém o HTML da página
response = requests.get(url)
html = response.text

# Cria o objeto BeautifulSoup para analisar o HTML
soup = BeautifulSoup(html, 'html.parser')

# Encontra a div específica pelo ID ou classe
div_content = soup.find('div', {'id': 'divContingencia'})  # Exemplo para um ID específico
# div_content = soup.find('div', {'class': 'classe_da_sua_div'})  # Exemplo para uma classe específica

# Exibe o conteúdo da div encontrada
if div_content:
    print('\nDiv encontrada')
else:
    print("Div não encontrada.")

if 'Não há estados com serviço de contingência ativo no momento.' in div_content.text:
    print('Não tem contingência')
else:
    print('Contingência está ativa pela SEFAZ')

estados = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 
           'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 
           'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']

if 'Não há agendamentos' in div_content.text:
    print('Não há contingência agendada :)')
else:
    estadosSefaz = soup.find('a', {'id': 'ctl00_ContentPlaceHolder1_gdvCtgAgendada_ctl02_hlkSefazAgendada'})
    inicioContingencia = soup.find('span',{'id':'ctl00_ContentPlaceHolder1_gdvCtgAgendada_ctl02_lblInicioCtgAgendada'})
    terminoContingencia = soup.find('span',{'id':'ctl00_ContentPlaceHolder1_gdvCtgAgendada_ctl02_lblFimCtgAgendada'})
    for estado in estados:
        if estadosSefaz.text == estado:
            print(f'Existe contingência agendada para {estado}')
            print(f'Início: {inicioContingencia.text}')
            print(f'Término: {terminoContingencia.text}')
            break