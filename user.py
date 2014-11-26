class user:
    username = None
    id = None
    firstname = None
    lastname = None
    avatarlink = None
    yearregistered = None
    lastlogin = None
    stateorprovince = None
    country = None
    traderating = None
    collection = None
    plays = None

    # def __init__(self):
        # print("Created a new user")

    def tostring(self):
        string = "USER {"
        string += "\n\tusername = {}".format(self.username)
        string += "\n\tid = {}".format(self.id)
        string += "\n\tfirstname = {}".format(self.firstname)
        string += "\n\tlastname = {}".format(self.lastname)
        string += "\n\tavatarlink = {}".format(self.avatarlink)
        string += "\n\tyearregistered = {}".format(self.yearregistered)
        string += "\n\tlastlogin = {}".format(self.lastlogin)
        string += "\n\tstateorprovince = {}".format(self.stateorprovince)
        string += "\n\tcountry = {}".format(self.country)
        string += "\n\ttraderating = {}".format(self.traderating)
        # collection = None
        # plays = None
        string += "\n}"
        return string
