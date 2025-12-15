import qrcode
import os

print("DANG O THU MUC:", os.getcwd())

img = qrcode.make("http://127.0.0.1:5000")
img.save("noel_qr.png")

print("TAO QR XONG")
