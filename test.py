from filters import BlurFilter
import cv2

image = cv2.imread("screenshot.png")
ni = image.copy()
f = BlurFilter()
cv2.imshow("1", image)
f.apply(image, ni)
cv2.imshow("2", ni)
cv2.waitKey(0)
cv2.destroyAllWindow()
