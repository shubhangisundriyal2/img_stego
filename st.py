import cv2
import os

img = cv2.imread("normalImage.png")

if img is None:
    print("Error: Image not loaded. Check the file path and format.")
    exit()

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

d = {chr(i): i for i in range(256)}
c = {i: chr(i) for i in range(256)}

height, width, _ = img.shape  # Get image dimensions
m = 0
n = 0
z = 0

for i in range(len(msg)):
    img[n % height, m % width, z] = d[msg[i]]
    n += 1
    m += 1
    z = (z + 1) % 3

cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")

message = ""
n, m, z = 0, 0, 0

pas = input("Enter passcode for Decryption: ")
if password == pas:
    for i in range(len(msg)):
        message += c[img[n % height, m % width, z]]
        n += 1
        m += 1
        z = (z + 1) % 3
    print("Decryption message:", message)
else:
    print("YOU ARE NOT AUTHORIZED!")
