def solver(a,b,c):
    D=(b**2)-4*a*c
    if D==0:
        x=-b/2*a
        return x
    elif D>0:
        x1=(-b+D**0,5)/2*a
        x2=(-b-D**0,5)/2*a
        return(x1,x2)
    else:
        return('нет корней')
print(solver(2,5,8))