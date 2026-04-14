class A:
 def m(self):print('instance')
 @classmethod
 def c(cls):print('class')
a=A();a.m();A.c()