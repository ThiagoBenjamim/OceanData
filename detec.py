import cv2
import time
from ultralytics import YOLO

# Cores para as caixas delimitadoras
COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0), (0, 0, 255), (255, 0, 255), (128, 0, 0), (0, 128, 0), (0, 0, 128)]

# Carregar o modelo YOLOv8 pré-treinado
model = YOLO('FishInv.pt')

# Obter os nomes das classes do modelo
class_names = model.names

# Inicializar a captura de vídeo
cap = cv2.VideoCapture("./fish.mp4") # Use 0 para a webcam padrão

if not cap.isOpened():
    print("Erro: Não foi possível abrir a câmera.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Erro: Não foi possível ler o frame da câmera.")
        break

    start = time.time()

    # Realizar a detecção com YOLOv8
    results = model.predict(frame, conf=0.25, iou=0.7, verbose=False)

    end = time.time()

    # Processar os resultados
    for r in results:
        boxes = r.boxes  # Bounding boxes e seus atributos
        for box in boxes:
            # Coordenadas da caixa delimitadora
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            
            # ID da classe e confiança
            class_id = int(box.cls[0])
            confidence = float(box.conf[0])

            # Desenhar a caixa delimitadora e o rótulo
            color = COLORS[class_id % len(COLORS)]
            label = f"{class_names[class_id]} : {confidence:.2f}"

            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
    
    # Calcular e exibir FPS
    fps_label = f"FPS: {1.0 / (end - start):.2f}"
    cv2.putText(frame, fps_label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 5)
    cv2.putText(frame, fps_label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Exibir o frame
    cv2.imshow("YOLOv8 Detections", frame)

    # Sair se a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar a câmera e destruir todas as janelas
cap.release()
cv2.destroyAllWindows()