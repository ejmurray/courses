import cv2

img=cv2.imread("galaxy.jpg", 0) #0 = grayscale | #1 = RGB | #-1 color with transparency

print()

resized_image=cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))
cv2.imshow("Galaxy", resized_image)
cv2.imwrite("Galaxy_resized.jpg", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()