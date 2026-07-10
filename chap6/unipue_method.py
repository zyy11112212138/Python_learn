a = 10
b = 20
print(dir(a))           #python中一切皆对象

print(a + b)
print(a.__add__(b))
print(a.__sub__(b))
print(f'{a} < {b}?',a.__lt__(b))
print(f'{a} <= {b}?',a.__le__(b))
print(f'{a} = {b}?',a.__eq__(b))
print('-'*40)
print(f'{a} > {b}?',a.__gt__(b))
print(f'{a} >= {b}?',a.__ge__(b))
print(f'{a} != {b}?',a.__ne__(b))
print('-'*40)
print(f'{a} * {b} =',a.__mul__(b))
print(f'{a} / {b} =',a.__truediv__(b))
print(f'{a} % {b} =',a.__mod__(b))
print(f'{a} // {b} =',a.__floordiv__(b))
print(f'{a} ^ 2 =',a.__pow__(2))
print('-'*40)