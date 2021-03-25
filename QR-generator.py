import png
import pyqrcode 
fonte = input("TEXTO OU URL AQUI: ")
file=input=("NOME PARA O SEU")
url = pyqrcode.create(fonte)
url.png("MeuCodigoQR.png",scale=6)