from . import xmlapi
from . import user
from . import collection
from . import plays

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

    def _buildPlayObject(self, xmlobj):
        playobj = plays.play()
        playobj.id = xmlobj.get('id')
        playobj.date = xmlobj.get('date')
        playobj.location = xmlobj.get('location')
        playobj.quantity = xmlobj.get('quantity')
        playobj.lengthInMinutes = xmlobj.get('quantity')
        playobj.nowinstats = xmlobj.get('nowinstats')
        playobj.incomplete = xmlobj.get('incomplete')
        playobj.itemid = xmlobj.findall('item')[0].get('objectid')
        commentobj = xmlobj.findall('comments')
        if len(commentobj) > 0:
            playobj.comments = commentobj[0].text
        for p in xmlobj.findall('player'):
            playerobj = plays.player()
            playerobj.username = p.get('username')
            playerobj.userid = p.get('userid')
            playerobj.name = p.get('name')
            playerobj.startposition = p.get('startposition')
            playerobj.color = p.get('color')
            playerobj.score = p.get('score')
            playerobj.rating = p.get('rating')
            playerobj.new = p.get('new')
            playerobj.win = p.get('win')
            playobj.players.append(playerobj)
        return playobj

    def getUserPlays(self, username):
        print("getUserPlays('%s')" % username)
        if username not in self.plays:
            userplays = plays.plays()
            xmlobj = xmlapi.requestPlaysForUser(username)

            for p in xmlobj.findall('play'):
                userplays.append(self._buildPlayObject(p))

            self.plays[username] = userplays
        return self.plays[username]

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
                imageobj = xmlitem.findall('image')
                if len(imageobj) > 0:
                    item.image = imageobj[0].text
                thumbnailobj = xmlitem.findall('thumbnail')
                if len(thumbnailobj) > 0:
                    item.thumbnail = thumbnailobj[0].text
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
