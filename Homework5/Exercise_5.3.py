# Create the generator random_walk(start) for a 1D random walker. If a position at a certain moment is x, then the next position can be x+1 or x-1 with equal probabilities.
# Find the final position after 100 moves (start=0).

import random

def random_walk(start):
    position = start
    while True:
        yield position
        step = random.choice([-1, 1])
        position += step

walker = random_walk(0)

pos = None
for _ in range(100):
    pos = next(walker)

print("Final position after 100 steps:", pos)

# Repeat experiments. 

def experiment(n_experiments=10, steps=100):
    results = []
    
    for _ in range(n_experiments):
        walker = random_walk(0)
        pos = None
        
        for _ in range(steps):
            pos = next(walker)
        
        results.append(pos)
    
    return results


# test
print(experiment(10, 100))
