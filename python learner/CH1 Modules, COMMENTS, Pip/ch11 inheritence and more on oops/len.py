class FavouriteGames:
    def __init__(self, games):
        self.games = games

    def __len__(self):
        return len(self.games)

obj = FavouriteGames(["GtaV", "Minecraft", "Palworld", "Nfs"])
print(len(obj)) 