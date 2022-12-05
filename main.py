from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open(input("Input your link: "))

result = decode(img)

print(result)