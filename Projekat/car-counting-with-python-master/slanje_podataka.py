
from firebase import firebase
import threading
from time import sleep

firebase = firebase.FirebaseApplication('https://iot-brojac-default-rtdb.firebaseio.com/',None)

br = 0
while(1):
    #br +=1
    f = open("dat.txt", "r")
    br = int(f.read())
    print(br)
    result = firebase.put("/IoT-Brojac","Vale",str(br))
    #print(br)
    sleep(2)
