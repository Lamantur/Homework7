class Road:

    def __init__(self, length, width) -> None:
        self._length = length
        self._width = width

    def MassForCoating(self):
        return f"{self._length*self._width*25*0.05/1000} т"


road = Road(6000, 20)
print(road.MassForCoating())
