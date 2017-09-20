import httplib2
import json

def getGeocodeLocation(inputString):
    # Use Google Maps to convert a location into Latitute/Longitute coordinates
    # FORMAT: https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=API_KEY
    google_api_key = "PASTE_YOUR_KEY_HERE"
    # replace all spaces with '+'
    locationString = inputString.replace(" ", "+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'
            % (locationString, google_api_key))
    # Create instance of the HTTP class
    h = httplib2.Http()
    
    # Create a GET request that returns an array with 2 values, 
    reponse, content = h.request(url,'GET')
    # Call jason.loads on content, to format it better
    result = json.loads(content)
    
    # Print to terminal
    print "response header: %s \n \n" %reponse

    return result
    # latitude = result['results'][0]['geometry']['location']['lat']
    # longitude = result['results'][0]['geometry']['location']['lng']
    # return (latitude,longitude)

getGeocodeLocation('Colombo Sri Lanka')