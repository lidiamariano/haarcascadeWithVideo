import cv2
import os

def frames_de_video():
    entrada = '/home/lidia/prova2_teste/assests/video_prova.mp4'
    caminho_saida = '/home/lidia/prova2_teste/assests'
    
    entrada_capturada = cv2.VideoCapture(entrada)
    cont = 0
    while entrada_capturada.isOpened():
        retorno, frame = entrada_capturada.read()

        if retorno:
            cv2.imwrite(os.path.join(caminho_saida, '%d.png') %cont, frame)
            cont +=1
        else:
            break
    cv2.destroyAllWindows()
    entrada_capturada.release()


frames_de_video()