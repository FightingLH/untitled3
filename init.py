class FooBar:
    def __init__(self,value):
        self.sonmevar = value
f = FooBar("hello everyone")
print  f.sonmevar

class A:
    def hello(self):
        print "hello I'm A"
class B(A):
    pass
b = B()
print b.hello()