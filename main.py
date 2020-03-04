from flask import Flask, render_template, request
import googlemaps
import random

api_key = ""

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    gmaps = googlemaps.Client(key=api_key)


    if request.method == 'POST' and 'location' in request.form:
        place = request.form['location']
        geo = gmaps.geocode(address=place)

        # print(geo)
        for item in geo:
            lat = ((item['geometry']['location']['lat']))
            lng = ((item['geometry']['location']['lng']))

            geo = str(lat) + ',' + str(lng)

        places_result = gmaps.places_nearby(location=geo, radius=8046, open_now=True, type='restaurant')

        places = []
        for item in places_result['results']:
            places.append((item['name']))

        place = random.choice(places)
        return render_template('index.html', place=place)

    return render_template('index.html')


# Take out for GCP
if __name__ == "__main__":
   app.run()