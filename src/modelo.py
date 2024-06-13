import cv2
import os

# Carregar o classificador pré-treinado
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Diretório contendo as imagens
input_dir = '/home/lidia/prova2_teste/frames/'
output_dir = '/home/lidia/prova2_teste/frames_detected/'

# Criar o diretório de saída se não existir
os.makedirs(output_dir, exist_ok=True)

# Iterar através das imagens numeradas de 0.png a 301.png
for i in range(302): 
    img_path = os.path.join(input_dir, f'{i}.png')
    img = cv2.imread(img_path)

    if img is None:
        print(f'Não foi possível ler a imagem: {img_path}')
        continue

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detectar rostos
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Desenhar retângulos em torno dos rostos detectados
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Salvar a imagem resultante
    output_path = os.path.join(output_dir, f'{i}_detected.png')
    cv2.imwrite(output_path, img)

    print(f'Processada e salva: {output_path}')
