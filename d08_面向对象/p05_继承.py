class Kaiyin:
    xueliang=100
    gongji=100
    
    def dazhao(self):
        print("凯隐大招")

    def __init__(self):
        print("创建了一个普通凯隐")

class Nanju:
    def zhufu(self):
        print("男爵buff")
    
    def __init__(self):
        print("一个奥恩")

#(里是父类)  可以多继承

class KaiyinBlue(Kaiyin,Nanju):
  
    def method1(self):
        pass  #占位 ,防止报错
    def dazhao(self):
        #重写写父类方法,又想用父类方法 super()
        super().dazhao()            
        print("现已升级为蓝凯隐大招")

    def __init__(self):
        
        print("创建了一个蓝色凯隐")
        
hero=KaiyinBlue()
hero.method1()
hero.dazhao() 
hero.zhufu()
print(hero.xueliang)