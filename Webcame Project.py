from ultralytics import YOLO
import cv2

# 1. Properly define the model using the YOLO class we imported
# (Using 'yolov8n.pt' as a standard lightweight model, it will auto-download)
model = YOLO("yolov8n.pt")

# 2. Open the webcam'

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # 3. Run YOLO inference on the frame
    results = model(frame)
    
    # 4. Plot the results on the frame (Note the square brackets [0])
    drawing = results[0].plot()
    
    # 5. Display the frame (imshow needs a window name first, then the image)
    cv2.imshow("YOLO Webcam", drawing)
    
    # Press 'q' on your keyboard to break the loop and close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 6. Clean up
cap.release()
cv2.destroyAllWindows()  # Capital 'W' fixed here


    
