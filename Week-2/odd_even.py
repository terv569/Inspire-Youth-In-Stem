number = 100
if (number % 2 == 0):
    print("even number")
else:
    print("odd number")

sum = 0
for i in range(0, 50):
    sum = sum + 2
    print(sum)











sum = 1
for i in range (0, 49):
    sum = sum + 2
    print(sum)






















#write a program to list all prime numbers from 1-100
primes = []
limit = 100


for n in range(2,limit+1):
    isprime = True
    for divisor in range(2,n):
        if n % divisor == 0:
            isprime = False
            break
if isprime:
    primes.append(n)


print(primes)