try:
    n=int(input())
    try:
        x=list(map(int,input().split(' ')))
        if(n==len(x)):
            for i in range(n):
                print(x[i],i,end="\n")
        else:
            print("Invalid input")
    except ValueError:
        print("Invalid input")
except ValueError:
    print("Invalid input")
