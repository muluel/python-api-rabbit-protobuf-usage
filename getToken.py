import requests, requests.auth
import env

CLIENT_ID = env.CLIENT_ID
CLIENT_SECRET = env.CLIENT_SECRET
USERNAME = env.USERNAME
PASSWORD = env.PASSWORD

auth = requests.auth.HTTPBasicAuth(CLIENT_ID,CLIENT_SECRET)
data = {
    "grant_type":"password",
    "username":USERNAME,
    "password":PASSWORD
}
headers = {"User-Agent":"Python-rabbit-protobuf-usage by %s" % USERNAME}

response = requests.post(
                    "https://www.reddit.com/api/v1/access_token",
                    auth = auth,
                    data = data,
                    headers = headers,
                )

TOKEN = response.json()['access_token']

print(TOKEN)