import urllib.request
from xml.etree.ElementTree import XML

NUM_PLAY_RECORDS_PER_PAGE = 100

# class xmlapi:
HOST = "https://www.boardgamegeek.com"
URL_COLLECTION = HOST + "/xmlapi2/collection"
URL_PLAYS = HOST + "/xmlapi2/plays"
URL_USERS = HOST + "/xmlapi2/users"

def _performRequest(url):
    response = urllib.request.urlopen(url)
    data = response.read() # a bytes object
    text = data.decode('utf-8')
    # print(text)
    xml = XML(text)
    return xml

def _processPlaysRequest(url):
    xmlobj = _performRequest(url + "&page=1")

    numrecords = float(xmlobj.get('total'))
    numremainingpages = int(numrecords / NUM_PLAY_RECORDS_PER_PAGE)
    # print("TRACE: xmlobj count = {}".format(len(xmlobj.findall('play'))))
    # print("TRACE: numrecords = {}".format(numrecords))
    # print("TRACE: numremainingpages = {}".format(numremainingpages))

    for page in range(2, numremainingpages+2):
        nextpage = _performRequest(url + "&page={}".format(page))
        for nextplay in nextpage.findall('play'):
            xmlobj.append(nextplay)
        # print("TRACE: xmlobj count = {}".format(len(xmlobj.findall('play'))))

    # TODO: verify that num play items == numrecords
    return xmlobj

def requestPlaysForUser(username):
    url = URL_PLAYS + "?username=" + username
    return _processPlaysRequest(url)

def requestCollectionForUser(username):
    url = URL_COLLECTION + "?username=" + username
    return _performRequest(url)

def requestUser(username):
    url = URL_USERS + "?name=" + username
    return _performRequest(url)
