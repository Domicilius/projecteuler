import math

solution = math.factorial(100)
solution = list(str(solution))
holder=0
for i in range(0,len(solution)):
    holder += int(solution[i])

print holder
