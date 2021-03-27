# strava_activity_type_changer
Changes the activity type for 'slow' activities to 'hike'.

## How to
* get all python requirements:
  * py -3 -m venv .venv
  * .venv\scripts\activate
  * pip install -r requirements.txt

* create your own strava API application
  * https://www.strava.com/settings/api.
  * put your strava client_id in ./private/client_id.txt  
  * put your strava client_secret in ./private/client_secret.txt

* run get_authorization.py 
    * a browser window will automatically open - give authorization
    * extract the 'code' from the redirected url and save it in ./private/client_code.txt

* set up some cut-off values in modify_activities.py
* run  modify_activities.py


## Resources
* Based on this tutorial
  * https://madflex.de/strava-update-gear-using-strava-api/
* Strava API documentation
  * https://developers.strava.com/
  * https://developers.strava.com/docs/getting-started/
  * https://developers.strava.com/docs/
  * https://developers.strava.com/docs/reference/
  * https://www.strava.com/settings/api

