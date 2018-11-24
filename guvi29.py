h=0
try:
    m=int(input())
    while(m>=60):
        h=h+1
        m=m-60
    print(h,m)
except ValueError:
    print("Invalid input")
