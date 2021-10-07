import pyrebase
import json

def upload():
    print('병원의 이름을 입력해주세요')
    name = input('▶')
    print('병원의 별점을 입력해주세요')
    rating = int(input('▶'))

    check1 = 0
    for i in old_version.each():
        if i.key() == name:
            x = db.child('Hospitals').child(name).get()
            
            check1 += 1
            
            check2 = 0
            for j in x.each():
                if j.key() == 'rating':
                    old_info = j.val()
                    
                    old_rating = old_info[0]
                    old_num = old_info[1]

                    new_rating = (old_rating * old_num + rating) / (old_num + 1)
                    new_num = old_num + 1

                    new_info['rating'] = [new_rating, new_num]
                    db.child('Hospitals').child(name).child('rating').remove()
                    db.child('Hospitals').child(name).update(new_info)

                    check2 += 1

            if check2 == 0: 
                new_info['rating'] = [rating, 1]
                db.child('Hospitals').child(name).update(new_info)
                
    if check1 == 0:
        return
    
    
def download(name):
    x = db.child('Hospitals').child(name).get()
    x = x.val()

    return round(x['info'][0])

with open('auth.json') as f:
    config = json.load(f)

firebase = pyrebase.initialize_app(config)
db = firebase.database()

old_version = db.child('Hospitals').get()
new_info = {}

upload()
