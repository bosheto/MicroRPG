import opensimplex

# opensimplex.seed(113)

# n = opensimplex.noise2(10, 10)
# print(n)

class World:

    def __init__(self, seed):
        self.seed = seed
        opensimplex.seed(seed)
        self.chunks = [[]]
        
    