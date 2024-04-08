class Kaiyin:
    xueliang=100
    gongji=100
    
    def dazhao():
        print("凯隐大招")

    def __init__(self):
        
        print("一个普通凯隐")
#(里是父类)
class KaiyinBlue(Kaiyin):
  
    
    def dazhao():
        print("蓝凯隐大招")

    def __init__(self):
        
        print("一个蓝色凯隐")
        
hero=KaiyinBlue
hero.dazhao() 
print(hero.xueliang)