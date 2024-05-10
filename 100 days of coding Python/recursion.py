def sum(n): #recursive method
    if n == 0: #base case
        return 0
    else: #recursion
        return n + sum(n-1)
def sum1(n): #iteration method
    result = 0
    for i in range(n+1):
        result += i
    return result
def sum2(n): #math method
    return n*(n+1)/2

print(sum1(4))
print(sum2(4))
print(sum(4))