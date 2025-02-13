

class Animal:
    def make_noise(self):
        print("Detta djur har vi inget ljud för.")


class Dog(Animal):
    def make_noise(self):
        print("Voff!")

class Cat(Animal):
    def make_noise(self):
        # super().make_noise()
        print("Mjau!")

class Rooster(Animal):
    def make_noise(self):
        print("Cock-a-doodle-do!")

class Goldfish(Animal):
    def make_noise(self):
        super().make_noise()


def sound_off(animal):
    animal.make_noise()


c = Cat()
d = Dog()
h = Rooster()
gf = Goldfish()

animals = [c, d, h, gf]

for animal in animals:
    sound_off(animal)

# sound_off(c)
# sound_off(d)
# sound_off(h)
# sound_off(gf)
