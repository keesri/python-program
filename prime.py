N = int(input("Enter a Number: "))

if N > 1:   # prime numbers are greater than 1
    for i in range(2, N):
        if N % i == 0:
            print("It is Not a Prime Number")
            break
    else:
        print("It is a Prime Number")
else:
    print("It is Not a Prime Number")
