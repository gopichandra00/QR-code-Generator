#QR code Generator
import qrcode as qr
img = qr.make("https://github.com/gopichandra00")
img.save("Gopi's_github.png")
