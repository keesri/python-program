N = int(input("Enter a Number: "))
result = 0

while N > 0:
    temp = N % 10         # get last digit
    result = result * 10 + temp
    N = N //  10           # remove last digit

print("Reversed Number:", result)



