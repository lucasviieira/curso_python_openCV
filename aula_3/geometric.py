# IMPORTANDO O OPENCV
import cv2

# ABRIR A IMAGEM
img = cv2.imread('./Orange.png')

# DESENHAR LINHA, parametros: (img, ponto1, ponto2, cor_em_BGR, espessura_linha) 
cv2.line(img, (10, 10), (200, 200), (0, 255, 0), 3)

# desenhar retangulo
cv2.rectangle(img, (10, 10), (200, 200), (255, 0, 0), 3)

# desenha circulo (se passar -1 na espessura, preenche o circulo)
cv2.circle(img, (200, 200), 50, (255, 0, 255), 3)

# desenha texto
cv2.putText(img, 'OpenCV', (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

# MOSTRAR A IMAGEM
cv2.imshow('img', img)

# PAUSA
cv2.waitKey(0)