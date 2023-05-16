def twice(g):
    return lambda x:g(g(x))
print(twice(twice)(twice(lambda x:-2*x))(2))