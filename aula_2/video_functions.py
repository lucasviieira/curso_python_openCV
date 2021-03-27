# IMPORTAR O OPENCV
import cv2

# CAPTURAR VIDEO
cap = cv2.VideoCapture(0)

# PERCORRER OS FRAMES DO VIDEO (LOOP INFINITO)
while(True):
    # RECUPERAR FRAME (RET DIZ SE CONSEGUIU PEGAR A IMAGEM)
    ret, frame = cap.read()

    # SE TEM RETORNO, MOSTRA O FRAME
    if ret:
        # MOSTRAR FRAME
        cv2.imshow('frame', frame)

        # CRIAR ROI
        roi = frame[100:500, 200:600]

        # MOSTRAR ROI
        cv2.imshow('roi', roi)
    
    # RECUPERA O BOTÃO APERTADO
    key = cv2.waitKey(10)

    if key == ord('q') or key == ord('Q'):
        break

# LIBERA O CACHE DO CAP
cap.release()

# DESTROI TODAS AS JANELAS ABERTAS
cv2.destroyAllWindows()