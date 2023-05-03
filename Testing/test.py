import addition
import pytest

def test_add():
    assert addition.add(4,5) == 9

def test_sub():
    assert addition.sub(4,5) == -1

#py -m pytest file.py::test_function

class A:
   def a(self):
       return "Function inside A"

class B:
   def a(self):
       return "Function inside B"

class C:
   pass

class D(C, A, B):
   pass

d = D()
print(d.a())