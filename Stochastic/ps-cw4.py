import math
from decimal import Decimal
album_numer = input("Wpisz numer albumu:")
ns = [int(i) for i in album_numer]
xmin = min(ns)
xmax = max(ns)
A = xmax
B = (1/5)*sum(ns)*1000
S0 = (xmin+2)*1e-4
m2 = ((2*math.pi)/(B))*S0*(A**2)
Py = ((A**2)/(B))**2
Pym2 = Py/m2

print(f"A = {A}")
print(f"B = {B} = {B:.2e}")
print(f"S0 = {S0} = {S0:.2e}")
print(f"K(w) = {A}*({2}*pi/{B})*rect(w-w0/{B})=({A*(2*math.pi)/(B):.2e}*rect(w-w0/{B}))")
print(f"m2 = (({2*math.pi:.2e})/({B}))*{S0:.2e}*({A**2:.2e})= {m2} = {m2:.2e}")
print(f"Py = ({(A**2):.2e}/{(B)})**2 = {Py} = {(Py):.2e}")
print(f"Py/m2  = {Py:.2e}/{m2:.2e} =  {Pym2} = {(Pym2):.2e} = {10*math.log10(Pym2)} dB = {10*math.log10(Pym2):.2e} dB")
