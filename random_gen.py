# MICHAEL VICTOR
# COMPUTER SCIENCE GROUP B
# 23/0749

class SimpleRandom:
    # Blueprint for a generator that makes pseudo-random numbers
    def __init__(self, seed):
        # Fixed constants used by the Linear Congruential Generator (LCG)
        self.a = 1103515245   # multiplier
        self.c = 12345        # increment
        self.m = 2**31        # modulus: results wrap around at this value

        # Remembered number. Starts at the seed, then changes on every call
        self.state = seed

    def next(self):
        # Compute the next state: multiply, add, then wrap with % m
        self.state = (self.a * self.state + self.c) % self.m

        # Scale the state into a decimal between 0 and 1
        return self.state / self.m

# Create a generator that starts from seed 42
rng = SimpleRandom(seed=42)
for i in range(5):
    print(rng.next())