


class Computer:
    def __init__(self, cpu, ram, storage):
       self.cpu = cpu
       self.ram = ram
       self.storage = storage
    def getDetails(self):
        print('from Computer class')
class Laptop(Computer):
    def __init__(self, cpu, ram, storage, screen, touch):
        super().__init__(cpu, ram, storage)
        self.screen = screen
        self.touch = touch
comp = Computer('i3', '8 GB', '500 GB')
print(comp.ram)
print(comp.cpu)
comp.getDetails()
lappy = Laptop('i5','16 gb', '256gb', '1080p', )