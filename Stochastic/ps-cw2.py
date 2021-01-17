import math
from decimal import Decimal
album_numer = input("Wpisz numer albumu:")
ns = [int(i) for i in album_numer]
alfa = (ns[1]+ns[3])/2*10**3
m2 = math.sqrt(max(ns))
S0 = (m2 * 2* alfa)/(alfa**2)
Bw = 2 * alfa
Bf = Bw/(2*math.pi) 
print(f"alfa = {Decimal(alfa):.2e}")
print(f"2alfa = {Decimal(2*alfa):.2e}")
print(f"alfa^2 = {Decimal(alfa**2):.2e}")
print(f"m2 = {m2} ~= {Decimal(m2):.2e}")
print(f"Sw = {m2:.2e}*{2* alfa:.2e}/w^2 + {alfa**2} = {(m2*2* alfa):.2e}/w^2 + {alfa**2:.2e} ")
print(f"S0 = {S0} ~= {Decimal(S0):.2e}")
print(f"Bw = {Bw}")
print(f"Bf = {Bf} ~= {Decimal(Bf):.2e}")
