import serial
import firebase_admin
from firebase_admin import credentials, firestore,db
import os, sys
import json
import ast
dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
robo = os.path.join(dirname, "robo.json")
cred = credentials.Certificate(robo)
firebase_admin.initialize_app(cred)
db = firestore.client()
arduinodata=serial.Serial('COM3',115200,timeout=2)

while 1:
    val=arduinodata.readline().decode('ascii')
    my_list = val.rstrip().split(",")
    if my_list != ['']:
        print(my_list)
        doc_ref = db.collection(u'tutorialfirebase-9ffa6').document('6UGVJGFVCvwOis1eJSjC')
        doc_ref.set({
            u'turbidity': 23,
            u'NOx': 11,
            u'TDS': 11,
            u'temp': 88,
        })