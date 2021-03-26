import requests

with open("private/client_id.txt") as f:
    CLIENT_ID = str(f.readline())

with open("private/client_secret.txt") as f:
    CLIENT_SECRET = str(f.readline())

with open("private/client_code.txt") as f:
    CLIENT_CODE = str(f.readline())

data = {
   "client_id": CLIENT_ID,
   "client_secret": CLIENT_SECRET,
   "code": CLIENT_CODE,
   "grant_type": "authorization_code",
}

response = requests.post(url="https://www.strava.com/oauth/token",
                         data=data)
response_j = response.json()

try:
    access_token = response_j["access_token"]
    with open("private/client_token.txt", "w") as f:
        f.write(access_token)
        print("Access token written succesfully.")
except KeyError: 
    print("Access_token not found - most probably a bad request. \nPrinting the entire json reply:")
    print(response_j)    

