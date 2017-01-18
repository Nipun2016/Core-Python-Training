class Foo(object):
  counter = 0
  def __call__(self):
    Foo.counter += 1
    return (Foo.counter)

foo = Foo()
a=foo() 
a=foo() 
a=foo()
print("Object Called : ",a)