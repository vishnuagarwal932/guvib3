try:
    n=int(input("enter a no. : "))
    if(1<=n<=100000):
        try:
            x=list(map(int,input().split(' ')))
            if(n==len(x)):
                x=sorted(x)
                if(len(x)%2!=0):
                    n=(n+1)//2
                    print(x[n-1])
                else:
                    n=n//2
                    a=float((x[n-1]+x[n])/2)
                    print(a)
                    
            else:
                print("Invalid input")
        except ValueError:
            print("Invalid input")
    else:
        print("Invalid input")
except ValueError:
    print("Invalid input")
