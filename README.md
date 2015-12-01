# Geocoding-Google-Python
25 line python script to geocoding addresses.

# Usage example:
        $> python get-coordinates.py 324 San Luis Oeste, san juan, argentina
        324 San Luis Oeste, san juan, argentina
        -31.5334842,-68.53081499999999
        
        $> python get-coordinates.py 50 balcarce, buenos aires, argentina
        50 balcarce, buenos aires, argentina
        -34.6083059,-58.371026799999996

I made this simple tool because the Google API limits the amount of geocode requests given a specific api key, and other services use Google API as well so it's pretty much the same.
If you don't understand how this thing works I'll put it in the following way:
  How many times can you search for "lol catz" in google? As many times as you want... this kind of geocoding uses the same principle
