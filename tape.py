class Tape():
    def __init__(self):
        """
        Pointer starts at first cell
        Tape starts out as all 0
        """
        self.thetape = [0]
        self.position = 0

    def get(self):
        return self.thetape[self.position]

    def set(self,val):
        self.thetape[self.position] = val

    def inc(self):
        self.thetape[self.position] += 1

    def dec(self):
        self.thetape[self.position] -= 1

    def advance(self):
        self.position += 1
        if len(self.thetape) <= self.position:
            self.thetape.append(0)

    def devance(self):
        self.position -= 1
        # """
        # If we are too far left the insert a 0
        # at the first element of the thetape
        # """
        # if not self.thetape[self.position]:
        #     self.thetape.insert(0, 0)
