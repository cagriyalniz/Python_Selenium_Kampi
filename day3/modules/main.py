from my_math import sum as topla
import random, sys
sys.path.insert(0,"..")
from class_exercise import Human

print(topla(random.randint(0, 5), random.randint(0, 5)))

human1 = Human("cagri")
human1.walk()