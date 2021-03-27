# importar openCV
import cv2

# funções
# não faz nada
def nothing(x):
    pass

# criar janela de trackbars
cv2.namedWindow('trackbars')

# criar as trackbars
cv2.createTrackbar('x', 'trackbars', 0, 800, nothing)
cv2.createTrackbar('y', 'trackbars', 0, 800, nothing)
cv2.createTrackbar('w', 'trackbars', 100, 800, nothing)
cv2.createTrackbar('h', 'trackbars', 100, 800, nothing)

# capturar video da webcam
cap = cv2.VideoCapture(0)

# loop para ficar pegando o frame
while (True):
    # recuperar trackbar
    x = cv2.getTrackbarPos('x', 'trackbars')
    y = cv2.getTrackbarPos('y', 'trackbars')
    w = cv2.getTrackbarPos('w', 'trackbars')
    h = cv2.getTrackbarPos('h', 'trackbars')

    # recupar o frame
    ret, frame = cap.read()

    # exibir o frame se conseguiu capturar
    if ret:
        # CRIAR ROI (Recorte da imagem)
        roi = frame[y:h, x:w]

        #exibir ROI
        cv2.imshow('roi', roi)
        
        # exibir frame
        cv2.imshow('frame', frame)

    # pausa
    if cv2.waitKey(10) == ord('q'):
        break

# liberar o cap
cap.release()

# destruir todas as janelas
cv2.destroyAllWindows()

