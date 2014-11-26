from enum import Enum

# itemsubtype = Enum('boardgame', 'boardgameexpansion', 'rpgitem', 'videogame'):
class itemsubtype(Enum):
  boardgame = 1
  boardgameexpansion = 2
  rpgitem = 3
  videogame = 4

class itemstatus:
    lastModified = None
    preordered = False
    wishlist = False
    wanttobuy = False
    wanttoplay = False
    want = False
    fortrade = False
    prevowned = False
    own = False

class item:
    id = -1
    name = None
    subtype = None
    yearpublished = 0
    image = None
    thumbnail = None
    status = None
    numplays = 0
    comment = None
    wishlistcomment = None

    def getAllPlays(self):
        return "TODO"

    def getAllPlaysForUser(self, user):
        return "TODO"

    def tostring(self):
        string = "ITEM {"
        string += "\n\tid = {}".format(id)
        string += "\n\tname = {}".format(name)
        string += "\n}"
        return string


class collection:
    user = None
    items = []
    lastModified = None

    def tostring(self):
        string = "COLLECTION: {"
        string += "\n\t{}".format(self.lastModified)
        string += "\n\t{}".format(self.user.tostring())
        string += "\n\titems = ({})".format(len(self.items))
        for i in items:
            string += "\n\t {}".format(i.tostring())
        string += "\n}"

        return string
