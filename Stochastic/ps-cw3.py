import math
from decimal import Decimal
album_numer = input("Wpisz numer albumu:")
ns = [int(i) for i in album_numer]
xmin = min(i for i in ns if i != 0)
xmax = max(ns)
a = 1/2*(xmin + xmax) + ns[2]
b = (xmin/xmax) + 1
C0 = 1/(xmax - xmin)
f = (xmax- xmin)/(2)
ymin = a*math.log(b*xmin)
ymax = a*math.log(b*xmax)
mx = (xmax + xmin)/(2)
my = (a*C0/b)*((math.exp(ymax/a)*((ymax/a)-1)) - (math.exp(ymin/a)*((ymin/a)-1)))
print(f"xmin = {xmin}")
print(f"xmax = {xmax}")
print(f"a = 1/2 *( {xmin} + {xmax} ) + {ns[2]} = {a}")
print(f"b = ({xmin}/{xmax}) + 1 = {b}")
print(f"C0 = {C0} = {(C0):.2e}")
print(f"mx = ({xmin} + {xmax})/2 ={mx} = {(mx):.2e}")
print(f"ymin = {a}*ln({b}*{xmin}) = {ymin} = {(ymin):.2e} ")
print(f"ymax = {a}*ln({b}*{xmax}) = {ymax} = {(ymax):.2e} ")
print(f"f(y) = {C0} * (1/abs({a}*{b}))*exp(y/{a}) = {C0} * (1/{abs(a*b)})*exp(y/{a}) = {C0*(1/abs(a*b))}*exp(y/{a})")
print(f"my  = ({a*C0/b})*((exp({ymax/a})*(({ymax/a})-1)) - (exp({ymin}/{a})*(({ymin}/{a})-1)) = {(a*C0/b)}*{((math.exp(ymax/a)*((ymax/a)-1)))} - {(math.exp(ymin/a)*((ymin/a)-1))} = {my} = {(my):.2e}")
