import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import sys
import time
import pybase64
import base64


# starting webcam

cap = cv2.VideoCapture(0)


names = []


# function for attendance file
fob = open('attendance.txt','a+')


def enterData(z):
    if z in names:
        pass
    else:
        names.append(z)
        z =''.join(str(z))
        fob.write(z+'\n')
    return names


print('PROCESSING WAIT.......')

#fuction data present or not

def checkData(data):
 data = str(data)
 if data in names:
    print('Present already marked')
 else:
    print('\n'+str(len(names)+1)+'\n'+'present done')
    enterData(data)



while True:
    _, frame = cap.read()
    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
            checkData(obj.data)
            time.sleep(1)


    cv2.imshow('Frame',frame)


 #closing
    if cv2.waitKey(1) &0xff==ord('s'):
      cv2.destroyAllWindows()
      break


f = open('attendance.txt','r')
lines = f.read().split("\n")


for i in range(0,len(lines)):
#  data = lines[i].decode()
  name = base64.b64decode(lines)





fob.close()

