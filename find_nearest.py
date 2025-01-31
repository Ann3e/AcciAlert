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

# Accident detected at latitude ,longitude
accident_location = (lat, lng)

nearest_hospital, hospital_dist = find_nearest(accident_location[0], accident_location[1], data["locations"],"hospital")
nearest_police, police_dist = find_nearest(accident_location[0], accident_location[1], data["locations"],"police_station")


print(f"Nearest Hospital: {nearest_hospital['name']} ({hospital_dist:.2f} km), Contact: {nearest_hospital['contact']}")
print(f"Nearest Police Station: {nearest_police['name']} ({police_dist:.2f} km), Contact: {nearest_police['contact']}")
