# Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br/')
except urllib.error.URLError:
    print('\033[31mO site Pudim não está acessível no momento.\033[m')
else:
    print('\033[32mConsegui acessar o site Pudim com sucesso!\033[m')



'''
import urllib
import urllib.request
import webbrowser

url = 'https://www.pudim.com.br/'

try:
    # 1. Tenta se conectar por "trás dos panos"
    urllib.request.urlopen(url) 
except urllib.error.URLError:
    # 2. Se a conexão falhar, avisa
    print('\033[31mO site Pudim não está acessível no momento.\033[m')
else:
    # 3. Se a conexão funcionar, avisa E ABRE o site
    print('\033[32mConsegui acessar o site Pudim! Abrindo...\033[m')
    webbrowser.open(url)'''