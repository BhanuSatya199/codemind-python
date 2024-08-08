integer=int(input())
rem=integer%10
while integer>9:
    integer=integer//10
print(rem+integer)