try:
    n=int(input())
    if(1<=n<=1000):
        try:
            x=list(map(int,input().split(' ')))
            if(n==len(x)):
                x=sorted(x)
                for i in range(n):
                    print(x[i],end=" ")

            else:
                print("invalid input")            
        except ValueError:
            print("invalid input")
    else:
        print("invalid input")
except ValueError:
    print("invalid input")
