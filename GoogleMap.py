import googlemaps
from datetime import datetime

if __name__ == "__main__":

    gmaps = googlemaps.Client(key='AIzaSyDImDc1pPOI2VTYG8Pb0xPedM8TuYHvI8A')

    # Geocoding an address
    addresses = ['1440 Wake Forest Drive, Davis, CA','250 W Quad, Davis, CA ']
    geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
    geocode_result_dict = {k: v for d in geocode_result for k, v in d.items()}
    print(geocode_result_dict['geometry']['location'])
    # Look up an address with reverse geocoding
    reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
    # Request directions via public transit
    now = datetime.now()
    directions_result = gmaps.directions("Sydney Town Hall",
                                        "Parramatta, NSW",
                                        mode="transit",
                                        departure_time=now)

    # Validate an address with address validation
    addressvalidation_result =  gmaps.addressvalidation(['1600 Amphitheatre Pk'], 
                                                        regionCode='US',
                                                        locality='Mountain View', 
                                                        enableUspsCass=True)