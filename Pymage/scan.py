from transform import four_point_transform
from skimage.filters import threshold_local
import numpy as np
import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True, help='Caminho para a imagem')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
ratio = image.shape[0]/500.0
orig = image.copy()
image = imutils.resize(image, height=500)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#gray = cv2.GaussianBlur(gray, (3,3),0)
edged = cv2.Canny(gray, 75,200)

print('PASSO 1: Detecção de bordas')
cv2.imshow('Imagem', image)
cv2.imshow('Bordas',edged)
cv2.waitKey(0)
cv2.destroyAllWindows()

cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]
for c in cnts:
	peri = cv2.arcLength(c,True)
	approx = cv2.approxPolyDP(c,0.02*peri,True)

	if len(approx)==4:
		screenCnt = approx
		break

print('PASSO 2: Encontrar o contorno do papel')
cv2.drawContours(image, [screenCnt], -1,(0,255,0),2)
cv2.imshow('Entorno papel', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

warped = four_point_transform(orig, screenCnt.reshape(4,2)*ratio)

warped = cv2.cvtColor(warped,cv2.COLOR_BGR2GRAY)
T = threshold_local(warped, 11,offset=10,method='gaussian')
warped = (warped>T).astype('uint8')*255

print('PASSO 3: Aplicar transformação de perspectiva')
cv2.imshow('Original', imutils.resize(orig,height=650))
cv2.imshow('Scaneada',imutils.resize(warped,height=650))
cv2.waitKey(0)
cv2.destroyAllWindows()