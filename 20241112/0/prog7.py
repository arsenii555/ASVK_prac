class A:
    def __init__(self, val):
        self.val = val
    
    def __str__(self):
        return f'<{self.val}>'


print(A(9))

class B(A):
    pass
