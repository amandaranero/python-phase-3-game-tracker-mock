from classes.result import Result

class Player:
    def __init__(self, username):
        username = str(username)
        if len(username)>=2 and len(username) <= 16:
            self.username = username

    def results(self):
        all = Result.get_all()
        return [res for res in all if res.player == self]

    def games_played(self):
        return [res.game for res in self.results()]

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        return len([res.score for res in self.results() if res.game == game])

    def add_result(self, game, score):
        Result(self, game, score)
        