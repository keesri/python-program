N = int(input("Enter a Number: "))
original = N    # store the original number
result = 0

while N > 0:
    temp = N % 10         # get last digit
    result = result * 10 + temp
    N = N // 10           # remove last digit

if original == result:
    print("It is a palindrome")
else:
    print("It is Not a palindrome")
