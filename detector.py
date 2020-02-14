import cv2
import numpy as np
# import for speech
#import pyttsx
#engine = pyttsx.init()
#engine.setProperty('rate', 70)
#voices = engine.getProperty('voices')
#for voice in voices:
 #engine.say("Hi there, Bibek")
#engine.runAndWait()
#import speech_recognition as sr
#r = sr.Recognizer()

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainner/trainner.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);


cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    #engine.say("Hello there, Could not recognize you.");
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        #print(Id)
        #print(conf)
        greeting_message="Hell"
        print(Id," ",conf)
        
        if(conf<90):
            if(Id==1):
                Id="Savan"
            elif(Id==2):
                Id="Bibek"
        else:
            Id="Unknown"
          
        
    cv2.imshow('im',im) 
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
