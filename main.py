import pyqrcode

qrcode_path = './qrcodes'

qr_string = input('Insert link to generate the QR Code: ')

url = pyqrcode.create(qr_string)

qrcode_name = input('Insert the file name (without extension): ')
qrcode_save = f'{qrcode_path}/{qrcode_name}.svg'

url.svg(qrcode_save, scale=8)

print(f"QR Code saved successfully at {qrcode_save}")
