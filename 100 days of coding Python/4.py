import random

#42
print(random.getrandbits(32)) # Get a random integer having 32 bits (2^32)
level = random.randint(1, 3)
print(level)
fl = random.random() * 5
print(fl)

#43
print("Tails or Heads?")
rand_side = random.randint(0, 1)
if rand_side == 0:
    print(f"It's tails {rand_side}")
else:
    print(f"It's heads {rand_side}")

