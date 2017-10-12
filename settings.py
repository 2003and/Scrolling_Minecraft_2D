class Settings:
    def __init__(self, game):
        if game == 'die':
            self.size = [50, 50]
            self.bg_color = (155, 100, 0)
            self.die_speed = 3
        elif game == 'card':
            self.width = 175
            self.height = 275
        elif game == 'minecraft':
            self.tilesize = 30
            self.playersize = 10
            self.mapwidth = 64
            self.mapheight = 30
            self.cloudwidth = 150
            self.cloudheight = 50
            self.cloudnum = 5
            self.maxfitx = 9
            self.maxfity = 5