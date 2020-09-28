import os
import requests

token = os.environ.get('YALIES_TOKEN')
def get_students():
    r = requests.post('https://yalies.io/api/students',
                      json={},
                      headers={
                          'Authorization': 'Bearer ' + token
                      })
    return r.json()

def get_image(student):
    filename = 'images/' + str(student['image_id']) + '.jpg'
    if student['image_id']:
        if not os.path.exists(filename):
            print('Downloading image ' + str(student['image_id']))
            r = requests.get(student['image'], stream=True)
            if r.ok:
                with open(filename, 'wb') as f:
                    for chunk in r:
                        f.write(chunk)
        else:
            print('Skipping ' + str(student['image_id']))

students = get_students()
print(students)
for student in students:
    get_image(student)
