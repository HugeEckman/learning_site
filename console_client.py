import requests
from requests.auth import HTTPBasicAuth
import base64
# from rest_framework.authtoken.models import Token
# from django.contrib.auth import admin
from learning_app.models import User


def send_request():
    # Basic auth

    url = 'http://127.0.0.1:8000/api/'
    username = 'admin'
    password = 'admin'

    response = requests.get(url, auth=(username, password))
    assert response.status_code == 200, response.status_code
    print(response.status_code)

def create_admin_token():
    user = User.objects(first_name='admin', last_name='adminovich', role_id=6)
    print(user)

if __name__ == '__main__':
    # send_request()
    create_admin_token()