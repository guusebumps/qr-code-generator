import pyqrcode
import png
from pyqrcode import QRCode

qrcode_path = './qrcodes'

# Link you wanna generate the qr code
qr_string = input('Insert link to generate the QR Code: ')

url = pyqrcode.create(qr_string)

# Makes the user choose a name for the file
qrcode_name = input('Insert the file name: ')
qrcode_save = f'{qrcode_path}/{qrcode_name}.png'

# Save the generated QR Code in the chosen path
url.png(qrcode_save, scale=8)