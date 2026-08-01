class Dinosaur:
    def __init__(self, name, period):
        self.name = name
        self.period = period

    def roar(self):
        return f"{self.name} says Roar!"
    
trex = Dinosaur("Tyrannosaurus Rex", "Cretaceous")
print(trex.roar())
teradactyl = Dinosaur("Pterodactyl", "Jurassic")
print(teradactyl.roar())
brontosaurus = Dinosaur("Brontosaurus", "Jurassic")
print(brontosaurus.roar())

