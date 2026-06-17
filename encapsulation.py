#encapsulation
#publicdata
'''class parent():
    publicdata=10
    def method1(self):
        print(self.publicdata)
class child(parent):
    def method2 (self):
        print(self.publicdata)
obj1=parent()
obj2=child()
obj1.method1()
obj2.method2()'''

#_protecteddata()
'''class parent():
    _protecteddata=100
    def method1(self):
        print(self._protecteddata)
class child(parent):
    def method2(self):
        print(self._protecteddata)
obj1=parent()
obj2=child()
obj1.method1()
obj2.method2()
print(obj1._protecteddata)
print(obj2._protecteddata)'''

#__privatedata()
'''class parent():
    __privatedata="aashika"
    def method1(self):
        print(self.__privatedata)
class child(parent):
    def method2(self):
        print(self._parent__privatedata)
obj1=parent()
obj2=child()
obj1.method1()
obj2.method2()'''

#abstraction
'''class A():
    def method1(self):
        pass
obj1=A()
obj1.method1()

class A():
    def method1(self):
        print("data")
obj1=A()
obj1.method1()

from abc import ABC,abstractmethod
class A(ABC):
    def method1(self):
        print("python")
obj1=A()
obj1.method1()'''

'''from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        print("python")
obj1=A()
obj1.method1()'''#error

from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        pass
    def method2(self):
        print("method2 is implemented")
    @abstractmethod
    def method3(self):
        pass
class B(A):
    def method1(self):
        print("method1 is implemented")
    def method3(self):
        print("method3 is implemented")

obj1=B()
obj1.method1()
obj1.method2()
obj1.method3()
