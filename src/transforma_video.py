import cv2

img = []

for i in range(302):
    imagem = cv2.imread(f'/home/lidia/prova2_teste/frames_detected/{i}_detected.png')
    if imagem is not None:
        img.append(imagem)
    else:
        print(f"Imagem {i}_detected.png não pôde ser lida.")

if len(img) == 0:
    print("Nenhuma imagem foi carregada.")
else:
    height, width, layers = img[0].shape

    fps = 30  # Aumenta o FPS para 30 para aumentar a velocidade do vídeo
    video = cv2.VideoWriter('video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    for image in img:
        video.write(image)

    video.release()
    cv2.destroyAllWindows()
    print("Vídeo criado com sucesso!")
