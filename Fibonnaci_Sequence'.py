def fib(num):
    if num == 1:
        return 0
    if num == 2:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)
 
    
 #Modify the value of fib_elin to find the the numbers at different positions   
    
fib_elin = 10
print("Fibonnaci sequence: ")
count = 1
for x in range(fib_elin):
    print(fib(count))
    count += 1

print("The number at position", fib_elin, "in the fibonacci sequence is", fib(fib_elin))