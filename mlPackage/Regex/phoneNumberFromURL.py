from urllib import request
from re import findall

url = 'https://www.summet.com/dmsi/html/codesamples/addresses.html'

response = urllib.reuest.urlopen(url)

html = response.read()

htmlstr = html.decode()

phndata = findall('\(\d{3}\) \d{3}-\d{4}',htmlstr)

for item in phndata:
    print item