This Python script allows you to generate QR codes from any link and save them as PNG files. It prompts the user to input a link and a name for the generated file, then saves the QR code image to a specified directory.

## Requirements

To run this script, you need to install the following dependencies:

- `pyqrcode`
- `pypng`

You can install them using pip:

```bash
pip install -r requirements.txt
```

## How to Use

1. Clone the repository or download the script.
2. Make sure you have the required dependencies installed (see above).
3. Run the script and follow the prompts:
```bash
python generate_qr.py
```
4. The script will ask you for:
* A link to generate the QR code.
* A name for the QR code file (without the extension).
The QR code will be saved as a PNG file in the ./qrcodes directory.

## Example

```bash
Insert link to generate the QR Code: https://github.com
Insert the file name: my_qrcode
```
The QR code image my_qrcode.png will be saved in the ./qrcodes folder.
