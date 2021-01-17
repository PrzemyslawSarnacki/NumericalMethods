import math
album_numer = input("Wpisz numer albumu:")
ns = [int(i) for i in album_numer]
xmin = min(ns)
xmax = max(ns)
n3 = ns[2]
l = 0.5*(xmin + xmax) + n3
c = 1/(l*(math.exp(-xmin/l) - math.exp(-xmax/l)))
m = -c*l*(math.exp(-xmax/l)*(xmax+l) - math.exp(-xmin/l)*(xmin+l))
print(f"xmin = {xmin}")
print(f"xmax = {xmax}")
print(f"lambda = {l}")
print(f"n3 = {n3}")
print(f"exp(-xmin/l) = {math.exp(-xmin/l)}")
print(f"exp(-xmax/l) = {math.exp(-xmax/l)}")
print(f"C0 = {c}")
print(f"m = {m}")