import requests
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    # res = 'http://127.0.0.1:8000/api-token-auth/'
    # data = {'username': 'Develop', 'password': '111111'}
    # response = requests.post(res, data=data)
    # print(response.json())
    token = '7df843a0a56bcabc6b49352c61c667498e512558'

    # res = 'http://127.0.0.1:8000/api/projects/'
    # auth = HTTPBasicAuth(username='Develop', password='111111')
    # response = requests.get(res, auth=auth)
    # print(response.json())

    res = 'http://127.0.0.1:8000/api/projects/'
    auth = HTTPBasicAuth(token=token)
    response = requests.get(res, auth=auth)
    print(response.json())
