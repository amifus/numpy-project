try:
    x=int(input("x:"))
    y=int(input("y:"))
    if x==y:
        print(f"{x}=={y}")
    a=2*x-3*y
    b=5
    if a==b:
        print("x=",x)
    g=int(input("what aretuype u want 1/ linage 2.square"))

    if g==1:
        p=x*y-2
    elif g==2:
        p=x**2-y*2-2
    print(p)
except ValueError: print("sosi")
