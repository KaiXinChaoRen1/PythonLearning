class Animal:
    def speak(self):
        pass            
   
class Dog(Animal):
    def speak(self):
        print("wangwang")

class Cat(Animal):
    def speak(self):
        print("miaomiao")   
        
def method(a):
    a.speak()
  
d= Dog()
c= Cat()  
method(d)
method(c)