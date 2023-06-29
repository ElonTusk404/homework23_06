def power_of(n):

    
    def power(x):
        return x ** n
    return power



result = power_of(2)
result_finish = result(5)
print(result_finish)