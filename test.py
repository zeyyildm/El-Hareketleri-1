import cv2

cap = cv2.VideoCapture(1)



if not cap.isOpened():
    print("Kamera açılamadı!")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Kamera çerçevesi alınamadı.")
        break

    cv2.imshow('Test Kamera', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

