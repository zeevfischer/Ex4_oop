from classes import Location

class agent:
    def __init__(self,id: int,value: float,src: int,dest: int,speed: float,pos: Location) -> None:
        self.id = id
        self.value = value
        self.src = src
        self.dest = dest
        self.speed = speed
        self.pos = pos

        self.nextpos = None
        self.time = float('inf')
        self.priorety = 0

    def relode(self, data: dict) -> None:
        self.id = int(data['id'])
        self.value = float(data['value'])
        self.src = int(data['src'])
        self.dest = int(data['dest'])
        self.speed = float(data['speed'])

        temp = str(data['pos'])
        loc = temp.split(',')
        self.pos = Location.Location(int(loc[0]), int(loc[1]), int(loc[2]))

        self.time = float('inf')
        self.priorety = 0
