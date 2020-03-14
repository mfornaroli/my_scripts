class Car:
    def __init__(self):
        self.speed = 0
    def accelerate(self, delta):
        self.speed += delta
    def __repr__(self):
        return "Car(speed = {0.speed})".format(self)

class Convertible(Car):
    def __init__(self):
        super().__init__()
        self.roof__open = False
    def open_roof(self):
        self.roof_open = True
    def close_roof(self):
        self.roof_open = False
    def __repr__(self):
        return "roof_open = {0.roof_open})".format(self)