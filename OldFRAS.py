import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
from cv2 import VideoCapture, imwrite
from datetime import datetime


l=s=[]
videoCaptureObject = VideoCapture(0)
model = tensorflow.keras.models.load_model('celebrity&empty.h5')
    
def readLabels():
    with open('celebrity&empty.txt','r')as f:
        for i in f:
            s=i.split(' ')
            l.append(s[1].strip('\n'))

def imageCapture():
    ret,frame = videoCaptureObject.read()
    imwrite("image.jpg",frame)
    videoCaptureObject.release()

def dateTime(x):
    now=datetime.now()	
    d= now.strftime("%d-%m-%Y")
    t= now.strftime("%H:%M:%S")
    s= str(d)+'.csv'
    time= str(t)+'\n'
    m= ""
    try:
        with open(s,'r') as f:
            m=f.read()
        with open(s,'w') as g:
            g.write(m)
            g.write(x+","+time)
    except FileNotFoundError:
        with open(s,'w+') as f:
            f.write(x+","+time)

def imageProcessing():
    np.set_printoptions(suppress=True)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open('image.jpg')
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    maxi=0.0
    p=0
    for i in range(len(prediction[0])):
        o=float(prediction[0][i])
        if (o>maxi):
            maxi=max(maxi,o)
            p=i
    print(l[p])
    dateTime(l[p])

readLabels()
imageCapture()
imageProcessing()

