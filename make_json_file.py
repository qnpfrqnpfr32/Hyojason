import json
from collections import OrderedDict

file_data = OrderedDict()

file_data["apiKey"] = "AIzaSyDJX6aXgw05YpSnfAmSWYBm80xrHjoPF_I"
file_data["authDomain"] = "ayaya-a123b.firebaseapp.com"
file_data["databaseURL"] = "https://ayaya-a123b-default-rtdb.firebaseio.com"
file_data["projectId"] = "ayaya-a123b"
file_data["storageBucket"] = "ayaya-a123b.appspot.com"
file_data["messagingSenderId"] = "110137030238"
file_data["appId"] = "1:110137030238:web:9f1d0ca47a4d11fd34e6cf"
file_data["measurementId"] = "G-QYTPSE1W21"

with open('ayaya.json', 'w', encoding="utf-8") as make_file:
    json.dump(file_data, make_file, ensure_ascii=False, indent="\t")
