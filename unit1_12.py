x=10
def f():
 global x;x=20
 def g():
  nonlocal x
 f()
print(x)