import requests

def get_full_address(address1, address2, city, state, country):
    full_address = ""

    if address1:
        full_address += address1
        full_address += " "

    if address2:
        full_address += address2
        full_address += " "

    if city:
        full_address += city
        full_address += " "

    if state:
        full_address += state
        full_address += " "

    if country:
        full_address += country
        full_address += " "

    return full_address

def get_lat_long(address):

    params = {
        'key': 'AIzaSyAdVP57aco-KOtMSFJHW4cBPgBvK3KG89I',
        'address': address
    }

    base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

    response = requests.get(base_url, params=params).json()
    response.keys()

    latitude = ''
    longitude = ''

    if response['status'] == 'OK':
        geometry = response['results'][0]['geometry']
        latitude = geometry['location']['lat']
        longitude = geometry['location']['lng']

    return {
        'latitude': latitude,
        'longitude': longitude,
    }