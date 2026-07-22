class Bird:
    def move(self): print('Bird moves')
class Sparrow(Bird):
    def move(self): print('Sparrow flies')
class Penguin(Bird):
    def move(self): print('Penguin swims')
for b in [Sparrow(),Penguin()]: b.move()
