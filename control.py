from . import xmlapi
from . import user
from . import collection

class control:
    collections = {}
    plays = {}
    users = {}

    def getUser(self, username):
        # print("getUser('%s')" % username)

        if username not in self.users:
            print("TRACE: performing user request")
            userobj = user.user()
            xmlobj = xmlapi.requestUser(username)

            userobj.username = xmlobj.get('name')
            userobj.id = xmlobj.get('id')
            userobj.firstname = xmlobj.findall('firstname')[0].get('value')
            userobj.lastname = xmlobj.findall('lastname')[0].get('value')
            userobj.avatarlink = xmlobj.findall('avatarlink')[0].get('value')
            userobj.yearregistered = xmlobj.findall('yearregistered')[0].get('value')
            userobj.lastlogin = xmlobj.findall('lastlogin')[0].get('value')
            userobj.stateorprovince = xmlobj.findall('stateorprovince')[0].get('value')
            userobj.country = xmlobj.findall('country')[0].get('value')
            userobj.traderating = xmlobj.findall('traderating')[0].get('value')

            self.users[username] = userobj

        return self.users[username]

    def getUserPlays(self, username):
        print("getUserPlays('%s')" % username)
        return "TODO"

    def getUserCollection(self, username):
        print("getUserCollection('%s')" % username)

        if username not in self.collections:
            print("TRACE: performing collection request")
        # usercollection = collection.collection()

        # self.collections[username] = collection

        return self.collections[username]
