Udacity Course - API's

Step 2: Add the API key to your application


* Google Maps - When loading the Google Maps Geocoding API, substitute YOUR_API_KEY in the code below with the API key you got from the previous step.
https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY

https://developers.google.com/maps/documentation/geocoding/get-api-key

* Foursquare -  Userless Server Integrations

Some of our endpoints that don’t pertain to specific user information, such as venues search are enabled for userless access (meaning you don’t need to have a user auth your app for access). To make a userless request, specify your consumer key's Client ID and Secret instead of an auth token in the request URL.

```javascript 
    https://api.foursquare.com/v2/venues/search?ll=40.7,-74&client_id=CLIENT_ID&client_secret=CLIENT_SECRET&query=pizza&v=YYYYMMDD
```

* Requesting From Python Code in `geocode.py`
  * Enter the python terminal in the vagrant machine with the `geocode.py` file.
  ```python
    >>> from geocode import getGeocodeLocation
    >>> getGeocodeLocation("Dallas, Texas")
    <!-- save response into a variable named dallas -->
    >>> dallas = getGeocodeLocation("Dallas, Texas")
    <!-- see keys of Dallas like a Dict and explore to find lat / long -->
    >>> dallas.keys 
    >>> dallas['results']
    >>> dallas['results'][0]['geometry']['location']['lat']
  ```

* Some Interesting APIs to Explore
  * Wikipedia API
  * StackExchange API
  * Google Maps API