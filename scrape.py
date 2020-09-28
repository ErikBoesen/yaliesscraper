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
    if student['image_id']:
        r = requests.get(student['image'], stream=True)
        if r.ok:
            with open('images/' + str(student['image_id']) + '.jpg', 'wb') as f:
                for chunk in r:
                    f.write(chunk)

students = get_students()
print(students)
for student in students:
    get_image(student)
