class Animal:
    def __init__ (self):
        self.eyes = 2

    def breathe(self):
        print("Inhale, exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("Moving in water.")

nemo = Fish()
nemo.swim() #Moving in water.
nemo.breathe() #Inhale, exhale
print(nemo.eyes) #2