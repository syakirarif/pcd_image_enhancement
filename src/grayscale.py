import cv2
img = cv2.imread('Contoh.jpg')
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('WarnaAbu.jpg', grayImage)
cv2.imshow('Menampilkan Gambar', grayImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
