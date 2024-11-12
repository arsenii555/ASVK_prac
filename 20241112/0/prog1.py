class A:
    v = 1


class B(A):
    v = 2

a, b = A(), B()
b.v = 3
print(f'b.v: {b.v}')
del b.v
print(f'b.v: {b.v}')
del B.v
print(f'b.v: {b.v}') 
 
