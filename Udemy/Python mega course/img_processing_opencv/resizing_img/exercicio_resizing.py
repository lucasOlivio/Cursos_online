import cv2
import glob

for img in glob.glob("*.jpg"):
    im = cv2.imread(img, -1)

    resized = cv2.resize(im, (250,250))
    cv2.imshow(img[:-4],resized)

    cv2.imwrite("resized_"+img, resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
