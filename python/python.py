class point():
    def __init__(self,x,y):
            self.y = y
            self.x = x
    def value (self):
        print(f"the value of {self.x} * {self.y} = {self.x * self.y}")



object = point(int(input('X : ')),int(input('X : ')))
object.value()

