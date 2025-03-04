import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.request.URLError:
    print('O site Pudim não está acessível no momento')
    print()
else:
    print('Consegui acessar o site Pudim com sucesso!')
    print(site.read())