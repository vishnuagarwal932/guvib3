n,a,d=input("enter the values of N, A, D of AP : ").split()
try:
    val=int(n),int(a),int(d)
    n,a,d=int(n),int(a),int(d)
    if(n>=1 and a<=100000 and d<=100000):
        b=float(n/2)
        sum=int(b*(2*a+(n-1)*d))
        print(sum)
    else:
        print("invalid")

except ValueError:
    print("invalid")
