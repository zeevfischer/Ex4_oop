from classes import Location


class agent:
    def __init__(self, id: int, value: float, src: int, dest: int, speed: float, pos: Location) -> None:
        self.id = id
        self.value = value
        self.src = src
        self.dest = dest
        self.speed = speed
        self.pos = pos
