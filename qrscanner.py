import qrcode
img=qrcode.make("http://www.geeksforgeeks.org/")
img.save("gfg1.jpg")

import cv2
d=cv2.QRCodeDetector()
val,points,straight_qrcode=d.detectAndDecode(cv2.imread("gfg1.jpg"))
print(val)
print(points)
print(straight_qrcode)
