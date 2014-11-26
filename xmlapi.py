import urllib.request
from xml.etree.ElementTree import XML

# class xmlapi:
HOST = "https://www.boardgamegeek.com"
URL_COLLECTION = HOST + "/xmlapi2/collection"
URL_PLAYS = HOST + "/xmlapi2/plays"
URL_USERS = HOST + "/xmlapi2/users"

def performRequest(url):
    response = urllib.request.urlopen(url)
    data = response.read() # a bytes object
    text = data.decode('utf-8')
    # print(text)
    xml = XML(text)
    return xml

def requestPlaysForUser(username):
    # url = URL_PLAYS + "?username=" + username + "&page=1"
    # Remember that need to retrieve multiple pages
    return "TODO"

def requestCollectionForUser(username):
    url = URL_COLLECTION + "?username=" + username
    return performRequest(url)

def requestUser(username):
    url = URL_USERS + "?name=" + username
    return performRequest(url)
