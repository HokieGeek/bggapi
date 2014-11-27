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
        string += "\n\tid = {}".format(self.id)
        string += "\n\tname = {}".format(self.name)
        string += "\n\tyearpublished = {}".format(self.yearpublished)
        string += "\n\timage = {}".format(self.image)
        string += "\n\tthumbnail = {}".format(self.thumbnail)
        string += "\n\tstatus = {}".format(self.status)
        string += "\n\tnumplays = {}".format(self.numplays)
        string += "\n\tcomment = {}".format(self.comment)
        string += "\n\twishlistcomment = {}".format(self.wishlistcomment)
        string += "\n}"
        return string


class collection:
    items = []
    lastUpdated = None

    def append(self, item):
        self.items.append(item)

    def tostring(self):
        string = "COLLECTION: {"
        string += "\n\t{}".format(self.lastUpdated)
        string += "\n\titems = ({})".format(len(self.items))
        for i in self.items:
            string += "\n\t{}".format(i.tostring())
        string += "\n}"

        return string
