import qrcode

data = input("Enter the text or the URL: ").strip()
filename = input("Enter the name of the file: ").strip()
qr = qrcode.QRCode(box_size=10, border = 4)
qr.add_data(data)
qr.make()
image = qr.make_image(fill_color="black", back_color="white")
image.save(filename)
print(f'QR Code Generated: {filename}')