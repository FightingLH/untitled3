import urllib,urllib2
import json
def check_api_get(url,data):
    data = urllib.urlencode(data)
    url2 = urllib2.Request(url,data)
    response = urllib2.urlopen(url2)
    print context
a = check_api_get("http://127.0.0.1/","1")