import requests

#Urls:
homework_url = 'https://www.classcharts.com/apipublic/homework'
login_url = 'https://www.classcharts.com/apiv2student/login'

# Login System: 
def login(code, dob):
	headers = {'User-Agent': 'Mozilla/5.0'}
	payload = {'code':code,'dob':dob,'remember_me': '1'}
	session = requests.Session()
	resp = session.post(login_url, headers=headers, data=payload)
	jsonResponse = resp.json()
	if jsonResponse["success"] == 0:
		print("Error while looging - Your date of birth or your login code is incorrect!")
	else:
		name = jsonResponse["data"]["name"]
		print(f"Signed in as {name}!")


login('', '')
