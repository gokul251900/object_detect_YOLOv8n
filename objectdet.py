from ultralytics import YOLO
import cv2
from tkinter import Tk, filedialog
import imgresize

img = imgresize.resize()
model = YOLO("yolov8n.pt")
res=model(img, show=True)
cv2.imshow("result", res[0].plot())
cv2.waitKey(0)
cv2.destroyAllWindows()