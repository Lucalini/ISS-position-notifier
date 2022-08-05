import requests
import time
from twilio.rest import Client
from datetime import datetime
account_sid = "REDACTED"
auth_token = "REDACTED"
my_phone_number = "REDACTED"
client = Client(account_sid, auth_token)
x=5
while x ==5:

    MY_LAT= 34.158710
    MY_LONG= -118.246580
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    print(data)

    iss_position = data["iss_position"]
    print(iss_position)

    longitude = float(iss_position["longitude"])
    latitude = float(iss_position["latitude"])
    paramenters= {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted":0,
}

    def is_close():
        global client
        global my_phone_number
        distance_lat = MY_LAT - latitude
        distance_lng = MY_LONG - longitude
        if distance_lat < 5 and distance_lat > -5:
            print(f" Close, {distance_lng}, {distance_lat}")
            client.messages.create(to=f"{my_phone_number}", from_= "+19785612449", body="The Space Station is overhead")
            return True

        elif distance_lng < 5 and distance_lng > -5:
            print(f" Close, {distance_lng}, {distance_lat}")
            return True
        else:
            print(f"Not Close, {distance_lng}, {distance_lat}")
            return False


    time.sleep(5)
    is_close()

# response = requests.get("https://api.sunrise-sunset.org/json", params= paramenters)
# data = response.json()
# sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
# sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
#
# print(sunrise)
# print(sunset)
# time_now=datetime.now()
# print(time_now.hour)
