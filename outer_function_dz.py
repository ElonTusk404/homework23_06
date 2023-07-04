def outer_function(x: int):
    def inner_function(factor):
        return x * factor
    return inner_function
    
one = outer_function(5)
two = one(2)
print(two)
