from firebase import firebase


firebase = firebase.FirebaseApplication('https://iot-brojac-default-rtdb.firebaseio.com/',None)

result = firebase.get('/IoT-Brojac/Vale', None)
print(result)