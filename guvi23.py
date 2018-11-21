n=input("enter a no : ")
try:
    v=int(n)
    n=int(n)
    if(1<=n<=100000):
        try:
            x = list(map(int, input().split(' ')))
            if(n==len(x)):
                a=min(x)
                print(a)
            else:
                print("invalid")
        except ValueError:
            print("invalid")
    else:
        print("invalid")
except ValueError:
    print("invalid")
