import math
#Exercicio 3: Baskara:

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))
#calculo de delta:
delta = b * b - 4 * a * c
print(delta)

if delta >= 0.0:
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    print(f"Para a equação de {a}x² + {b}x + {c} = 0, obtivemos os seguintes valores: x1 = {x1} e x2 = {x2}")
elif delta == 0.0:
    x1 = (-b + math.sqrt(delta))/(2*a)
    print(f"Para a equação de {a}x² + {b}x + {c} = 0, obtivemos o seguinte valor para x = {x1}")
else:
    print(f"Para a equação de {a}x² + {b}x + {c} = 0, não existem valores reais para x.")



