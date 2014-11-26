import urllib.request
from xml.etree.ElementTree import XML

# class xmlapi:
HOST = "https://www.boardgamegeek.com"
URL_COLLECTION = HOST + "/xmlapi2/collection"
URL_PLAYS = HOST + "/xmlapi2/plays"
URL_USERS = HOST + "/xmlapi2/users"

def performRequest(url):
    return "TODO"

def requestPlays():
    return "TODO"

def requestCollection():
    return "TODO"

def requestUser(username):
    url = URL_USERS + "?name=" + username
    response = urllib.request.urlopen(url)
    data = response.read() # a bytes object
    text = data.decode('utf-8')
    xml = XML(text)
    return xml
