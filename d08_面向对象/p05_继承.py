class Kaiyin:
    xueliang=100
    gongji=100
    
    def dazhao(self):
        print("凯隐大招")

    def __init__(self):
        print("一个普通凯隐")

class Nanju:
    def zhufu(self):
        print("男爵buff")
    
    def __init__(self):
        print("一个奥恩")

#(里是父类)  可以多继承

class KaiyinBlue(Kaiyin,Nanju):
  
    
    def dazhao(self):
        print("蓝凯隐大招")

    def __init__(self):
        
        print("一个蓝色凯隐")
        
hero=KaiyinBlue()
hero.dazhao() 
hero.zhufu()
print(hero.xueliang)