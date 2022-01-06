from classes import Location
class pokimon:

    def __init__(self,value,type: int,pos: Location):#agent):
        self.value = value
        self.type = type
        self.pos = pos
        self.src = None
        self.dest = None
        self.is_taken = False
        # self.agent = agent

    def relode(self,data: dict):
        self.value = data['value']
        self.type = data['type']

        temp = str(data['pos'])
        loc = temp.split(',')
        tap = (int(loc[0]), int(loc[1]), int(loc[2]))
        self.pos = Location.Location(tap)

    def __repr__(self) -> str:
        return str((self.src, self.dest))

    """
    this function will find the Edge the pokimon is on
    note: the type will tell me if it is from 1 to 2 or 2 to 1
    y=mx+b 
    """
    def is_Edge(self,x1,y1,x2,y2,type_Edge):
        epsilon = 0.00000001

        m = (float(y1)-float(y2)) / (float(x1)-float(x2))
        b = float(y1) - (m*float(x1))

        check1 = float(self.pos.y)
        check2 = (m * float(self.pos.x)) + b

        if abs(check1 - check2)<epsilon and type_Edge == self.type:
            return True
        else:
            return False




