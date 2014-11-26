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
            # print("TRACE: performing user request")
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
        # print("getUserCollection('%s')" % username)

        if username not in self.collections:
            # print("TRACE: performing collection request")

            usercollection = collection.collection()
            xmlobj = xmlapi.requestCollectionForUser(username);

            for xmlitem in xmlobj.findall('item'):
                item = collection.item()
                item.id = xmlitem.get('objectid')
                item.subtype = xmlitem.get('subtype')
                item.name = xmlitem.findall('name')[0].text
                yearpublishedobj = xmlitem.findall('yearpublished')
                if len(yearpublishedobj) > 0:
                    item.yearpublished = yearpublishedobj[0].text
                # item.yearpublished = xmlitem.findall('yearpublished')[0].text
                imageobj = xmlitem.findall('image')
                if len(imageobj) > 0:
                    item.image = imageobj[0].text
                # item.image = xmlitem.findall('image')[0].text
                thumbnailobj = xmlitem.findall('thumbnail')
                if len(thumbnailobj) > 0:
                    item.thumbnail = thumbnailobj[0].text
                # item.thumbnail = xmlitem.findall('thumbnail')[0].text
                item.numplays = xmlitem.findall('numplays')[0].text

                item.status = None

                commentobj = xmlitem.findall('comment')
                if len(commentobj) > 0:
                    item.comment = commentobj[0].text
                wishlistcommentobj = xmlitem.findall('wishlistcomment')
                if len(wishlistcommentobj) > 0:
                    item.wishlistcomment = wishlistcommentobj[0].text

                usercollection.append(item)

            self.collections[username] = usercollection

        return self.collections[username]
