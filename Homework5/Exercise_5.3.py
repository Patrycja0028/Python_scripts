import random

def random_walk(start):
    position = start
    while True:
        yield position
        step = random.choice([-1, 1])
        position += step


# pojedynczy eksperyment (100 kroków)
walker = random_walk(0)

pos = None
for _ in range(100):
    pos = next(walker)

print("Final position after 100 steps:", pos)




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
