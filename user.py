from datetime import datetime, timedelta


class User:
    characterSlots = 5

    def __init__(self, userid, corecolor, UTCtime):
        self.ID = userid
        self.Core_Color = corecolor
        self.Last_Core_Up = UTCtime
        self.Next_Core_Up = UTCtime + timedelta(weeks=cores[corecolor])
