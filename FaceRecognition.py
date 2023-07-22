from PIL import Image, ImageDraw, ImageFont
# from keras.models import load_model
from keras_facenet import FaceNet
import numpy as np
from numpy import asarray
from numpy import expand_dims
import face_recognition
import pickle
import cv2
import pyttsx3
from GetFaceLocation import face_recog

MyFaceNet = FaceNet()
# def voice_setting():
#     engine = pyttsx3.init() #初始化语音引擎
#     engine.setProperty('rate', 200)   #设置语速
#     engine.setProperty('volume',0.7)  #设置音量
#     voices = engine.getProperty('voices') 
#     engine.setProperty('voice',voices[0].id)   #设置第一个语音合成器
def predict(signature, database):
    min_dist=100
    identity=' '
    for key, value in database.items() :
        dist = np.linalg.norm(value-signature)
        if dist < min_dist:
            min_dist = dist
            identity = key
    return identity, min_dist

def Recognition(Training_Data, dictionary_ForName):
    ## voice
    engine = pyttsx3.init() #初始化语音引擎
    engine.setProperty('rate', 200)   #设置语速
    engine.setProperty('volume', 4)  #设置音量
    voices = engine.getProperty('voices') 
    engine.setProperty('voice',voices[0].id)   #设置第一个语音合成器
    # Rec
    cap = cv2.VideoCapture(0)
    all_id = []
    voice_his = []
    while True:
        _, gbr1 = cap.read()
        # print(gbr1.shape)
        # gbr1 = cv2.resize(gbr1, (320, 240))
        # print(gbr1.shape)
        # face_coordinate = face_recog(gbr1)  # 臉的座標
        face_coordinate = face_recog(gbr1)  # 臉的座標
        # live_img = Image.fromarray(cv2.cvtColor(gbr1, cv2.COLOR_BGR2RGB))         
        live_img = Image.fromarray(cv2.cvtColor(gbr1, cv2.COLOR_BGR2RGB))         
        draw = ImageDraw.Draw(live_img)
        font = ImageFont.truetype('simsun.ttc', 30, encoding = 'utf-8')

        if face_coordinate is not None:
            for(top, right, bottom, left) in face_coordinate:
                gbr = cv2.cvtColor(gbr1, cv2.COLOR_BGR2RGB)
                # print("gbr:", gbr.shape)
                gbr = Image.fromarray(gbr)                  # konversi dari OpenCV ke PIL
                gbr_array = asarray(gbr)
                face = gbr_array[top:bottom, left:right]
                # print("face:", face.shape)                  
                face = Image.fromarray(face)                       
                face = face.resize((160,160))
                face = asarray(face)
                # print(face.shape)
                face = expand_dims(face, axis=0)
                # signature = MyFaceNet.predict(face)
                signature = MyFaceNet.embeddings(face)

                # cv2.rectangle(gbr1, (left, top), (right, bottom), (0, 0, 255), 2)            # 標記人臉外框
                id, dist=predict(signature, Training_Data)
                if dist < 0.62:
                    id = str(id)
                    id = id.split(".")[0]        # 學號
                    all_id.append(id)
                    text = dictionary_ForName[id]  # return 學號對照的人名
                    voice = text
                    voice_his.append(voice)
                    # 若該學生出現超過2次則記為出席並喊聲簽到
                    if voice_his.count(voice) == 2:
                        engine.say(voice + "已簽到")
                else:
                    text = "?"
                print(text)
                # 
                # live_img = Image.fromarray(cv2.cvtColor(gbr1, cv2.COLOR_BGR2RGB))
                #     #
                # draw = ImageDraw.Draw(live_img)
                #     #
                # font = ImageFont.truetype('simsun.ttc', 30, encoding = 'utf-8')
                draw.rectangle(((left, top), (right, bottom)), fill = None, outline = 'green', width = 3 )
                    #
                draw.text((left - 10, top - 30), text, font = font, fill = (0,255,0))
                    #
        img = cv2.cvtColor(np.array(live_img), cv2.COLOR_RGB2BGR)
                #
        cv2.namedWindow('live', cv2.WINDOW_NORMAL)

                
            #全螢幕
            # cv2.namedWindow('live', cv2.WINDqOW_NORMAL)
        cv2.setWindowProperty('live', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow('live',img)
        engine.runAndWait()
        engine.stop()
        if cv2.waitKey(5) == ord('q'):
            break    # 按下 q 鍵停止
    cv2.destroyAllWindows()
    cap.release()
    return all_id
def attend(all_id):
    attend_students = []
    for i, u in enumerate(np.unique(all_id)):
        if all_id.count(u) > 1 :
            attend_students.append(u)
    return attend_students
# if __name__ == '__main__':
#     Recognition()
#     attend()
