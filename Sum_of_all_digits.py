integer=int(input())
sum_=0
while integer>0:
    rem=integer%10
    integer=integer//10
    sum_=sum_+rem
print(sum_)