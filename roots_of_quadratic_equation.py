import math

a = int(input("a = ?"))
b = int(input("b = ?"))
c = int(input("c = ?"))
x1 = int(input("x1 = ?"))
x2 = int(input("x2 = ?"))

d = math.pow(b,2)-4*a*c
if d >= 0:
    r1 = (-b+math.sqrt(d))/(2*a)
    r2 = (-b-math.sqrt(d))/(2*a)
    print("Roots: ",r1,",",r2)
else:
    rp = b/(2*a)
    ip = math.sqrt(-d)/(2*a)
    print("Roots: ",rp,"+j",ip,",",rp,"-j",ip)
