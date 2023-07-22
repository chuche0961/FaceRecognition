import os
from PIL import Image
from numpy import asarray
from numpy import expand_dims
import tensorflow.keras as keras
from keras_facenet import FaceNet
import numpy as np
import face_recognition
import pickle
import cv2
import matplotlib.pyplot as plt
from GetFaceLocation import face_recog
MyFaceNet = FaceNet()
def Live_embedding():
    myfile = open("TrainingData/TrainingData.pkl", 'rb')
    # myfile = open("TrainingData/TrainingData_NewEmbedding.pkl", 'rb')
    Training_Data = pickle.load(myfile)
    myfile.close()
    ids = []
    names = []
    faces = []
    count = 0
    database = {}
    cap = cv2.VideoCapture(0)
    id = input("Enter your ID : ")
    name = input("Enter your name : ")
    print("Plz Rotate your face")
    Ready = input("Are u Ready ?")
    while Ready is not '1':
        Ready = input("Are u Ready ?")
    while True:
        ret, img = cap.read()
        face_coordinate = face_recog(img)  # 臉的座標
        count += 1
        if face_coordinate is not None:
            for(top, right, bottom, left) in face_coordinate:
                face_BGR = img[top:bottom, left:right] # 彩色臉部
                face_RGB = cv2.cvtColor(face_BGR, cv2.COLOR_BGR2RGB)   
                gbr = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                gbr = Image.fromarray(gbr)                  # konversi dari OpenCV ke PIL
                gbr_array = asarray(gbr)
                face = gbr_array[top:bottom, left:right]                         
                face = Image.fromarray(face)                       
                face = face.resize((160,160))
                face_array = asarray(face)
                face_input = expand_dims(face_array , axis=0)   # face_array(160, 160) to face_array(1, 160, 160)
                    # signature = MyFaceNet.predict(face)
            face_feature = MyFaceNet.embeddings(face_input)
            faces.append(face_RGB)
            database[id + '.' +str(count)] = face_feature
            cv2.namedWindow('live', cv2.WINDOW_NORMAL)
            cv2.setWindowProperty('live', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.imshow('live',img)
        # if cv2.waitKey(300) == ord('q') or count == 20 :
        if cv2.waitKey(100) == ord('q') or len(faces) == 20 :
            break    # 按下 q 鍵停止
    cv2.destroyAllWindows()
    cap.release()
    # Show all pics
    faces = np.array(faces)
    fig, axes = plt.subplots(2, 10 , figsize = (15, 3))
    axes = axes.flatten()
    for i, u in enumerate(faces):
        axes[i].imshow(u)
        axes[i].set_xticks([])
        axes[i].set_yticks([])
    plt.show()
    print((len(database)))
    print(len(Training_Data))
    # 將原資料集與新增資料合併
    Training_Data.update(database)
    # 存檔
    myfile = open('TrainingData/TrainingData.pkl', 'wb')
    pickle.dump(Training_Data, myfile)
    myfile.close()
    # 更新ID對照表
    myfile = open('ID_Table/TrainingData_DicForID.pkl', 'rb')
    dictionary_ForName = pickle.load(myfile)
    myfile.close()
    ids.append(id)
    names.append(name)
    NewEmbbeding_ID_Dic = dict(zip(ids, names))
    # 合併新對照表
    New_dic = dictionary_ForName.update(NewEmbbeding_ID_Dic)
    # 存檔
    myfile = open('ID_Table/TrainingData_DicForID.pkl', 'wb')
    pickle.dump(dictionary_ForName, myfile)
    myfile.close()
    print("Number of faces : ", len(Training_Data))
    print(New_dic)

if __name__ == '__main__':
    Live_embedding()