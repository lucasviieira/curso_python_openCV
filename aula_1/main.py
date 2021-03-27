# IMPORTANDO O OPENCV
import cv2

# ABRIR A IMAGEM
img = cv2.imread('./Orange.png')

# MOSTRAR A IMAGEM
cv2.imshow('imagem', img)

# SALVAR NOVA IMAGEM
cv2.imwrite('nova.png', img)

# CRIAR ROI (Recorte da imagem)
roi = img[75:250, 100:300]

# MOSTRAR ROI
cv2.imshow('roi', roi)

# REDIMENSIONAR IMAGEM
imgResize = cv2.resize(img, (600, 600))

# MOSTRAR ROI
cv2.imshow('imgResize', imgResize)

# PAUSA
cv2.waitKey(0)