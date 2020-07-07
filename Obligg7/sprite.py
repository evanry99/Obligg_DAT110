class Sprite:
    neste_ID = 1

    def __init__(self, x_start, y_start, bredde, hoyde):
        self.x_start = float(x_start)
        self.y_start = float(y_start)
        self.bredde = 0
        self.set_bredde(bredde)
        self.hoyde = 0
        self.set_hoyde(hoyde)
        self.id = Sprite.neste_ID
        Sprite.neste_ID += 1

    @property
    def get_bredde(self):
        return self.bredde

    def set_bredde(self, ny_bredde):
        if ny_bredde >= 0:
            self.bredde = ny_bredde
        else:
            raise ValueError("Bredde kan ikke være negativ!")

    @property
    def get_hoyde(self):
        return self.hoyde

    def set_hoyde(self, ny_hoyde):
        if ny_hoyde >= 0:
            self.hoyde = ny_hoyde
        else:
            raise ValueError("Høyde kan ikke være negativ!")

    def areal(self):
        areal = self.bredde * self.hoyde
        return areal

    def er_inni(self, x_koordinat, y_koordinat):
        return not (x_koordinat < self.x_start
                    or y_koordinat < self.y_start
                    or x_koordinat > self.x_start + self.bredde
                    or y_koordinat > self.y_start + self.hoyde)

    def flytt(self, delta_x, delta_y):
        self.x_start += delta_x
        self.y_start += delta_y
