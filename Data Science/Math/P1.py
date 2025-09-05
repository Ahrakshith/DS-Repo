import numpy as np
from sympy import symbols,diff

y=symbols('y')

f=y*y+4*y+6

diff_val=diff(f,y)

print(diff_val)



