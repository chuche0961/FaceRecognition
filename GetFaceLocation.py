import face_recognition
import cv2
import matplotlib.pyplot as plt
def face_recog(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # gray = cv2.resize(gray, (320, 240))
    
    # plt.imshow(gray)
    # plt.show()
    # 進行人臉檢測, face_locations = 人臉座標
    face_locations = face_recognition.face_locations(gray,model="hog")  
    # 繪製人臉檢測結果
    if len(face_locations) == 0:
        face_locations = None
        print("No face")
    
    return face_locations