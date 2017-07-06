import urllib,urllib2
import json
def check_api_get(url,data):
    data = urllib.urlencode(data)
    url2 = urllib2.Request(url,data)
    response = urllib2.urlopen(url2)
    apicontent = response.read()
    context = json.loads(apicontent)
    retcode = context['data']
    print context

class data(object):
    def __init__(self):
        # self.appType = '0'
        # self.channelID = 'itunes'
        # self.device = '0'
        # self.deviceID = '2b6aaf651d5c31db217fecb43382bac8c03549701ee41cfa875d07362f16c283'
        # self.deviceVersion = '9.3.5'
        # self.isVip = '1'
        # self.isYn = '0'
        # self.language = 'ch'
        # self.lastID = lastID
        # self.newLastID = newLastID
        # self.signature = 'c1812012765d84443532157d17c7ccd8'
        # self.token = '58794fddaa7b9b6ac213d2d3a5455e8f'
        # self.uid = '9525475'
        # self.uniqueID = '5BE153CC-7452-4F75-8D99-0253C5529D35'
        # self.userLevel = '2'
        # self.version = '4.0.7'
def convert_data(obj):
    dict = {}
    dict.update(obj.__dict__)
    print dict
    return dict
