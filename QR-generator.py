import png
import pyqrcode 
fonte = input("TEXTO OU URL AQUI: ")
url = pyqrcode.create(fonte)
url.png("MeuCodigoQR.png",scale=6)
