class player:
    username = None
    userid = None
    name = None
    startposition = None
    color = None
    score = None
    rating = None
    new = False
    win = False

    def tostring(self):
        string = "PLAYER {"
        string += "\n\tusername = {}".format(self.username)
        string += "\n\tuserid = {}".format(self.userid)
        string += "\n\tname = {}".format(self.name)
        string += "\n\tstartposition = {}".format(self.startposition)
        string += "\n\tcolor = {}".format(self.color)
        string += "\n\tscore = {}".format(self.score)
        string += "\n\trating = {}".format(self.rating)
        string += "\n\tnew = {}".format(self.new)
        string += "\n\twin = {}".format(self.win)
        string += "}"
        return string

class play:
    id = None
    date = None
    location = None
    quantity = None
    lengthInMinutes = None
    nowinstats = False
    incomplete = False
    itemid = None
    comments = None
    players = []

    def tostring(self):
        string = "PLAY {"
        string += "\n\tid = {}".format(self.id)
        string += "\n\tdate = {}".format(self.date)
        string += "\n\tlocation = {}".format(self.location)
        string += "\n\tquantity = {}".format(self.quantity)
        string += "\n\tlengthInMinutes = {}".format(self.lengthInMinutes)
        string += "\n\tnowinstats = {}".format(self.nowinstats)
        string += "\n\tincomplete = {}".format(self.incomplete)
        string += "\n\titemid = {}".format(self.itemid)
        string += "\n\tcomments = {}".format(self.comments)
        for player in self.players:
            string += "\n\t{}".format(self.player.tostring)
        string += "\n}"
        return string

class plays:
    plays = []
    lastUpdates = None

    def append(self, play):
        self.plays.append(play)

    def tostring(self):
        string = "PLAYS {"
        string += "\n\tlastUpdates = {}".format(self.lastUpdates)
        for play in self.plays:
            string += "\n\t{}".format(play.tostring())
        string += "\n}"
        return string
