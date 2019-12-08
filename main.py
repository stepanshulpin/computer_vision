import cv2, numpy as np

filename = 'source_image.png'
img = cv2.imread(filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

contrast = cv2.equalizeHist(gray)
cv2.imshow("Contrast", contrast)

canny = cv2.Canny(gray, 70, 200)
cv2.imshow("Canny", canny)

corner = canny
tmp = np.float32(canny)
tmp = cv2.cornerHarris(tmp, 2, 3, 0.04)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
tmp = cv2.dilate(tmp, kernel)
corner[tmp > 0.01 * tmp.max()] = 255
cv2.imshow("Corner", corner)

dist = cv2.distanceTransform(corner, cv2.DIST_L2, 3)
cv2.normalize(dist, dist, 0, 1.0, cv2.NORM_MINMAX)
cv2.imshow("Distance", dist)

int_img = cv2.integral(gray)
res = gray
k = 1
size = (k * dist).astype('int32')
for x in range(gray.shape[0]):
    for y in range(gray.shape[1]):
        i = x + 1
        j = y + 1
        T = size[i - 1][j - 1]
        if T % 2 == 1:
            T += 1
        while (i - T / 2 < 0) or (j - T / 2 < 0) or (i + T / 2 + 1 > gray.shape[0]) or (j + T / 2 + 1 > gray.shape[1]):
            T -= 1
        if T > 0:
            A = int_img[int(i - T / 2)][int(j - T / 2)]
            B = int_img[int(i - T / 2)][int(j + T / 2 + 1)]
            C = int_img[int(i + T / 2 + 1)][int(j - T / 2)]
            D = int_img[int(i + T / 2 + 1)][int(j + T / 2 + 1)]

            res[i - 1][j - 1] = (A + D - B - C) / (T * T)
cv2.imshow("Average", res)
cv2.imwrite("result_image.png", res)

cv2.waitKey(0)
cv2.destroyAllWindows()
