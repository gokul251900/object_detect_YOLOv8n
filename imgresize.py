import cv2
import imgload
def resize():
    file_path = imgload.load_img()
    img = cv2.imread(file_path)
    resized_img = cv2.resize(img, (740, 420))
    return resized_img
