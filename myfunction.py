x = 10
def my_function():
    x = 20
    print(x)
    print(globals()['x'])
my_function()
