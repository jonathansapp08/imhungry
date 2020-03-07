from flask import Flask, render_template, request
import googlemaps
import random

api_key = ""

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Set up client
    gmaps = googlemaps.Client(key=api_key)

    # Get info from form
    if request.method == 'POST' and 'location' in request.form:
        place = request.form['location']
        geo = gmaps.geocode(address=place)

        for item in geo:
            lat = ((item['geometry']['location']['lat']))
            lng = ((item['geometry']['location']['lng']))

            geo = str(lat) + ',' + str(lng)

        # Get list of open places within 5 mile radius
        places_result = gmaps.places_nearby(location=geo, radius=8046, open_now=True, type='restaurant')

        # Only get names and location of place
        places = []
        for item in places_result['results']:
            places.append(     [   (item['name']),(item['geometry']['location']) ]         )

        # Pick only one place
        place = random.choice(places)

        # Get the address of place
        latlng = str(place[1]['lat']) + ',' + str(place[1]['lng'])
        address_result = gmaps.reverse_geocode(latlng=latlng)
        address= []
        for item in address_result:
            address.append(item['formatted_address'])


        return render_template('index.html', place=place[0], address=address[0])
    return render_template('index.html')

# Take out for GCP
if __name__ == "__main__":
   app.run()