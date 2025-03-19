import json

def load_credentials():
    with open ('D:\stepic_Cred.json', 'r') as file:
        credentials = json.load(file)
        return credentials
    


cred = load_credentials()
login = cred['login_stepik']
passwd = cred['password_stepik']
