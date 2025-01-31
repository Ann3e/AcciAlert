from twilio.rest import Client

trial='+919179826586'
import keys

def send_sms():
    client = Client(keys.account_sid, keys.auth_token)

    message_body = (
        f"🚨 Accident Alert 🚨\n"
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

# Call the function to send SMS
send_sms()