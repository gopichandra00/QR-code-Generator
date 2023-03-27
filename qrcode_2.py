import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=20, border = 3)
#
urs=qr.add_data(input("Please enter url\t"))
print(urs)
qr.make(fit=True)
img =  qr.make_image(fill_color="black",back_color="white")
img.save("qrcode_.png")

