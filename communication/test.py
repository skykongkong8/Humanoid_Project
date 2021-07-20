class animal():
    def __init__(self, num):
        self.num = num
class bird(animal):
    def __init__(self,num):
        super().__init__(num) 
        pass
    def numcheck(self):
        return self.num
pigeon = bird(1)
print(pigeon.numcheck())