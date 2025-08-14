import math
from rocket import Rocket

foguete1 = Rocket()
foguete2 = Rocket()

print(foguete1.x)
print(foguete1.y)
print(foguete2.x)
print(foguete2.y)

foguete1.move_rocket(2, 3)
foguete1.print_rocket()

foguete2.move_rocket(5, 7)
foguete2.print_rocket()