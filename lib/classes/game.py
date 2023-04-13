from classes.result import Result

class Game:
    def __init__(self, title):
        title = str(title)
        self.title = title

    def get_title(self):
        return self._title

    def set_title(self, title):
        if len(title)>0 and not hasattr(self, "title"):
            self._title = title

    title = property(get_title, set_title)

    def results(self):
        all = Result.get_all()
        return [res for res in all if res.game == self]

    def players(self):
        return [res.player for res in self.results()]

    def average_score(self,player):
        return sum([res.score for res in self.results() if res.player == player]) / len(self.players())