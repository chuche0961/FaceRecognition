# FaceRecognition
- Simply run the "RollCallSystem.py" file and ensure that the required objects for importing in other PY files have been installed prior to execution. These objects include "face_recognition," "cv2," "pyttsx3," "tensorflow," and "matplotlib.pyplot."

- The "TrainingData.pkl" file contains training data for myself and my 32 classmates. If you wish to include additional data, execute "RollCallSystem.py" and respond with "1" when prompted with "U wanna add a new one?" (To decline, input "0"). Follow by entering the ID and name to add a new face for recognition.


# FaceRecognition
- 只需要運行"RollCallSystem.py"檔即可 ,
在運行之前先看看其他PY檔中需要import的物件是否已經install ,
像是 face_recognition , cv2 , pyttsx3 , tensorflow , matplotlib.pyplot ... 

- TrainingData.pkl 裡面的訓練是我及我的32位同學， 若想新增， 運行"RollCallSystem.py"時，
  會跑出"U wanna add a new one?" 回答 1(不想新增回答0) ，輸入ID及姓名就可新增人臉加入辨識

# 摘要

- 在這篇研究文章中，我們探討了利用人臉辨識技術來加速教師點名的速度。我
  們希望解決傳統點名方法所需的長時間以及其效率低下的問題，期望透過應用人臉
  辨識的技術，使點名過程變得更加迅速且準確。為此，我們打算設計一個基於人臉
  辨識的點名系統。
  在分析方法部分，我們分為人臉辨識和人臉偵測兩個部分。在人臉辨識方面，
  本研究首先選擇使用與機器學習相關的統計方法，包括 K-近鄰算法(K-Nearest
  Neighbors, KNN)、支持向量機(Support Vector Machines, SVM)、隨機森林分類器
  (Random Forest Classifier, RFC)，以及深度學習的方法包括 Facenet 和 ArcFace 的深
  度殘差網路(ResNet)進行人臉辨識。人臉偵測方面，我們實驗了哈爾特徵(Haar
  features)、主成分分析(Principal Component Analysis, PCA)、線性判別分析(Linear
  Discriminant Analysis, LDA)、局部二值模式(Local Binary Patterns, LBP)、方向梯度
  直方圖(Histogram of Oriented Gradients, HOG)和單一尺度特徵金字塔(Single Shot
  MultiBox Detector, SSD)進行人臉偵測。
  在經過測試之後，Facenet 的實驗中達到了約 90%的準確率，而 ArcFace 的實驗
  準確率約 85%。在人臉偵測方面，我們發現 HOG 和 SSD 能最準確地偵測到人臉，
  而 HOG 能更快速地偵測到人臉，且能夠擷取到極端的人臉，這更符合我們點名系
  統的需求。因此，我們最終選擇使用 Facenet 和 HOG 來設計一個人臉辨識點名系
  統。該系統將使用手機鏡頭來進行人臉辨識。另外，我們還在此人臉辨識系統中加
  入了語音功能，教師只需要使用手機掃描學生的臉部，學生則能透過語音獲知自己
  是否被點名，系統就能自動識別出學生的身份，並記錄他們的出席情況。
