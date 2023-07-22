from GetFaceLocation import face_recog
from Live_Embedding import Live_embedding
from Training_Data import Data
from FaceRecognition import  predict, Recognition, attend
from Web import Web
import pickle

# 載入模型
# MyFaceNet = FaceNet()

# 決定訓練資料，得到Embedding資料和對照表
Training_Data, dictionary_ForName = Data()
# Embedding_other = input("Do U want to add another member ?")
# if Embedding_other == 1:
#     Training_Data, dictionary_ForName = Data()
# 開始辨識，獲得所有辨識出的ID並存成list
all_id = Recognition(Training_Data, dictionary_ForName)


# 若list裡該學生的學號出現超過3次即視為出席
attend_students = attend(all_id)
print(attend_students)

# 儲存出席學生列表
myfile = open('attend_students.pkl', 'wb')
pickle.dump(attend_students, myfile)
myfile.close()

# 透過網頁查看出席狀況
Web(dictionary_ForName, attend_students)

