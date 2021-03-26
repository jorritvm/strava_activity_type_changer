import requests
from scrapy import Selector
import webbrowser as wb


with open("private/client_id.txt") as f:
    CLIENT_ID = str(f.readline())

params = {
    "client_id": CLIENT_ID,
    "response_type": "code",
    "redirect_uri": "http://localhost",
    "approval_prompt": "force",
    "scope": 'read,activity:read,activity:write',
}

response = requests.get("http://www.strava.com/oauth/authorize", params=params, allow_redirects=False)
sel = Selector(response)
url_auth = sel.xpath("/html/body/a/@href").extract_first()
wb.open_new(url_auth)
