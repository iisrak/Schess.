from events import Events

class CheckHandler():

    def __init__(self):

        Checked = Events()
        Checked.on_change += KingCheckHandler

        self.WhiteKingChecked = False
        self.BlackKingChecked = False


    def KingCheckHandler(self):
        pass