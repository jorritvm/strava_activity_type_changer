import requests

AMOUNT_OF_PAGES = 1
AMOUNT_OF_ACTIVITIES_PER_PAGE = 3
MAX_SPEED_CAP = 20.0 # km/h
AVG_SPEED_CAP = 7.5 # km/h

with open("private/client_id.txt") as f:
    CLIENT_ID = str(f.readline())

with open("private/client_secret.txt") as f:
    CLIENT_SECRET = str(f.readline())

with open("private/client_code.txt") as f:
    CLIENT_CODE = str(f.readline())

with open("private/client_token.txt") as f:
    CLIENT_TOKEN = str(f.readline())

headers = {
   "Authorization": f"Bearer {CLIENT_TOKEN}"
}

for page in range(1, AMOUNT_OF_PAGES + 1):
    print("Fetching activities from page " + str(page))
    params = {"per_page": AMOUNT_OF_ACTIVITIES_PER_PAGE, "page": page}
    result = requests.get(url="https://www.strava.com/api/v3/athlete/activities",
                          params=params, headers=headers)
    print("Found %i activities." % len(result.json()))
    for item in result.json():
        id = item.get("id")
        print("Evaluating http://www.strava.com/activities/" + str(id))

        if (item.get("type") != "Hike" and 
            item.get("average_speed") < (AVG_SPEED_CAP / 3.6) and 
            item.get("max_speed") < (MAX_SPEED_CAP / 3.6)):
            
            print("\t <-- This activity was probably a hike, so the script modified it")

            # update the type
            activity = requests.put(url=f"https://www.strava.com/api/v3/activities/{item.get('id')}",
                                    data={"type": "Hike"},
                                    headers=headers)

print("Finished successfully.")