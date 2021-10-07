from selenium import webdriver
import pyrebase
import json

hospital_list = []

def crawling(department):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    
    driver = webdriver.Chrome(options=options)
    url = 'https://www.naver.com/'
    driver.get(url)

    elem1 = driver.find_element_by_id('query')
    elem1.send_keys('송도 ' + department)

    elem2 = driver.find_element_by_id('search_btn')
    elem2.click()

    elem3 = driver.find_elements_by_class_name('QLp9G')

    for i in elem3:
        hospital_list.append(i.text)

    for i in hospital_list:
        new_info = {}
        
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        
        driver = webdriver.Chrome(options=options)
        
        url = 'https://www.naver.com/'
        driver.get(url)

        elem1 = driver.find_element_by_id('query')
        elem1.send_keys('송도 ' + i)

        elem2 = driver.find_element_by_id('search_btn')
        elem2.click()

        elem3 = driver.find_elements_by_class_name('_1mAZf')

        x = []
        cnt = 0
        for j in elem3:
            phone_number = ''
            if cnt == 2:
                break
            elif cnt == 0:
                for m in j.text:
                    if m in '0123456789-':
                        phone_number += m
                x.append(phone_number)
                cnt+=1
            else:   
                x.append(j.text)
                cnt+=1
                
        new_info['info'] = x
        db.child('Hospitals').child(i).set(new_info)

def main():
    print('================')
    print('1. 안과')
    print('2. 이비인후과')
    print('3. 내과')
    print('4. 신경외과')
    print('5. 정형외과')
    print('6. 피부과')
    print('7. 항문외과')
    print('================')
    print()
    print('가야할 진료과를 입력해주세요')
    answer = int(input('▶'))
    print()

    if answer == 1:
        crawling('안과')
    elif answer == 2:
        crawling('이비인후과')
    elif answer == 3:
        crawling('내과')
    elif answer == 4:
        crawling('신경외과')
    elif answer == 5:
        crawling('정형외과')
    elif answer == 6:
        crawling('피부과')
    elif answer == 7:
        crawling('항문외과')

with open('auth.json') as f:
    config = json.load(f)

firebase = pyrebase.initialize_app(config)
db = firebase.database()

main()
