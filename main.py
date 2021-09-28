import requests

#Urls:
# Homework URL: https://www.classcharts.com/apipublic/homework
# Login URL: https://www.classcharts.com/apiv2student/login

login_url = 'https://www.classcharts.com/apiv2student/login'
headers = {'User-Agent': 'Mozilla/5.0'}
payload = {'code':'codehere','dob':'dobhere'}
session = requests.Session()
session.post(login_url, headers=headers, data=payload)
