from PIL import Image
from numpy import asarray
from numpy import expand_dims
import tensorflow.keras as keras
from keras_facenet import FaceNet
import numpy as np
import face_recognition
import pickle
import cv2
from GetFaceLocation import face_recog
from Live_Embedding import Live_embedding

# 載入模型
MyFaceNet = FaceNet()
def Data():
    while True:
    # 決定是否要現場新增辨識成員
        AddNew_Ornot = input("U wanna add a new one?")
        if AddNew_Ornot == '1':
            Live_embedding()
            Data_path = 'TrainingData/TrainingData.pkl'
            ID_table = 'ID_Table/TrainingData_DicForID.pkl'
        elif AddNew_Ornot == '0':
            Data_path = 'TrainingData/TrainingData.pkl'
            ID_table = 'ID_Table/TrainingData_DicForID.pkl'
            break
    print(Data_path)

    # 載入 Embedding 後的訓練集
    myfile = open(Data_path, 'rb')
    Training_Data = pickle.load(myfile)
    myfile.close()
    print(len(Training_Data))
    # 載入學號對照表
    myfile = open(ID_table, 'rb')
    dictionary_ForName = pickle.load(myfile)
    myfile.close()
    print(dictionary_ForName)

    return Training_Data, dictionary_ForName

if __name__ == '__main__':
    Data()