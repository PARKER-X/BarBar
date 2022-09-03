import cv2
img = cv2.imread("static/image/pic_Jlt9nX7.jpg", cv2.IMREAD_COLOR)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()