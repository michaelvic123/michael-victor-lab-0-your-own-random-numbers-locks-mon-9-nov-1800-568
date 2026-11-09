# MICHAEL VICTOR
# COMPUTER SCIENCE GROUP B
# 23/0749

from random_gen import SimpleRandom # Import the generator class from random_gen.py
rng = SimpleRandom(seed=123)

# Simulate rolling a die n times
def simulate_die_rolls(n):
    total = 0
    for _ in range(n):
        # Convert random [0,1) to die roll [1,6]
        roll = int(rng.next() * 6) + 1
        total += roll
    return total / n

# Roll 10, 100, 1000, and 10000 times
for n in [10, 100, 1000, 10000]:
    average = simulate_die_rolls(n)
    print(f"Average of {n:5d} rolls: {average:.4f}")