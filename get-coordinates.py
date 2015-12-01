try:
  import requests
except:
  print "You need the Requests module"
  print "You can install it with PIP"
  exit()
from re import search,sub
from sys import argv
from string import join

print join(argv[1:],' ')

if len(argv) > 2: direccion = join(argv[1:],'%20')
elif len(argv) == 2: direccion = sub(' ','%20',argv[1])
else:
  print "Usage example: python get-coordenadas.py 324 San Luis Oeste, san juan, argentina"
  exit()

url = "https://www.google.com.ar/maps/place/%s" %direccion
headers = {'Host':'www.google.com.ar','User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', 'Connection':'keep-alive'}

r = requests.get(url, headers=headers)
response = r.text

try:
  coordenadas = search('(?<=markers=)-[0-9]{1,2}.[0-9]+%2C-[0-9]{1,2}.[0-9]+(?=&amp)',response.split('\n')[0]).group(0).split('%2C')
  print coordenadas[0] +','+coordenadas[1]
except:
  print "Error"
