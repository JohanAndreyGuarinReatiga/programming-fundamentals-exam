#area del triangulo equilatero

import math

a = int(input("ingrese el lado del triangulo: ")) 
A = (math.sqrt(3) / 4) * math.pow(a, 2)
if A > 1000:
    print("DATOS NO VÁLIDOS")
else:
    print(f"""El area del triangulo es: {A}""")