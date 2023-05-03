class A:
    def a(self):
        return "Function inside A"
    
class B:
    def a(self):
        return "Function inside B"

class C():
    def a(self):
        return "Function inside C"
    
class D(A,B):
    def a(self):
        return 'Function inside D'

class E(B,C):
    def a(self):
        return "Function inside E"
    
class F(E,D,C):
    pass

f = F()
print(f.a())
print(F.mro())