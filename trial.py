import cv2 as cv
import numpy as np

# img = cv.imread("image.png")
# cv.imshow("image", img)
# cv.waitKey(0)
# cv.destroyAllWindows()

# img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# print(img_hsv)
# img_hsv[0:100] = (100000, 255, 255)
# print(img_hsv.shape)
# img_hsv = cv.cvtColor(img_hsv, cv.COLOR_HSV2BGR)
# cv.imshow("image", img_hsv)
arr = np.fromfunction(lambda i, j, _: (i // 100 + j // 100) * 8 + 400,
                      (600, 800, 3))
arr[:, :, 1] = 175
arr[:, :, 2] = 150
arr = cv.cvtColor(arr.astype(np.uint8), cv.COLOR_HSV2BGR)
cv.imshow("image", arr)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imwrite("mosaic_bg.png", arr)
