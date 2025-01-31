from geopy.distance import geodesic
import json


# Load database of hospitals and police stations
with open("data.json", "r") as file:
    data = json.load(file)

def find_nearest(lat, lon, services,type):
    nearest_service = None
    min_distance = float("inf")

    for service in services:
        if(type==service["type"]):
            service_location = (service["latitude"], service["longitude"])
            distance = geodesic((lat, lon), service_location).km
            if distance < min_distance:
                min_distance = distance
                nearest_service = service

    return nearest_service, min_distance

# Example: Accident detected at latitude 28.6139, longitude 77.2090
accident_location = (28.6139, 77.2090)

nearest_hospital, hospital_dist = find_nearest(accident_location[0], accident_location[1], data["locations"],"hospital")
nearest_police, police_dist = find_nearest(accident_location[0], accident_location[1], data["locations"],"police_station")


print(f"Nearest Hospital: {nearest_hospital['name']} ({hospital_dist:.2f} km), Contact: {nearest_hospital['contact']}")
print(f"Nearest Police Station: {nearest_police['name']} ({police_dist:.2f} km), Contact: {nearest_police['contact']}")




from twilio.rest import Client

trial='+919179826586'
import keys

def send_sms():
    client = Client(keys.account_sid, keys.auth_token)
    
    message_body = (
        # f"🚨 Accident Alert 🚨\n"
        f"Location: {accident_location}\n"
        f"google_maps_url = https://www.google.com/maps?q={accident_location[0]},{accident_location[1]}\n"
        f"Nearest Hospital: {nearest_hospital['name']} ({nearest_hospital['contact']})\n"
        f"Nearest Police: {nearest_police['name']} ({nearest_police['contact']})\n"
        f"⚠️ Immediate Assistance Required!"
    )

    # Send SMS to the hospital
    hospital_sms = client.messages.create(
        # body=message_body, from_=TWILIO_PHONE_NUMBER, to=nearest_hospital["contact"]
        body=message_body, from_=keys.TWILIO_PHONE_NUMBER, to=trial

    )

    # Send SMS to the police station
    police_sms = client.messages.create(
        # body=message_body, from_=TWILIO_PHONE_NUMBER, to=nearest_police["contact"]
        body=message_body, from_=keys.TWILIO_PHONE_NUMBER, to=trial

    )

    print("✅ SMS sent successfully!")
    # print(f"📩 Hospital SMS SID: {hospital_sms.sid}")
    # print(f"📩 Police SMS SID: {police_sms.sid}")

# Call the function to send SMS


send_sms()