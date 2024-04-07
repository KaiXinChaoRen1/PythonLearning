class Hero:
    __hp = 100
    __mp = 100

    def __checkmp(self):
        if self.__mp < 50:
            return False
        else:
            return True

    def dazhao(self):
        if self.__checkmp():
            print("德玛西亚!")
        else:
            print(f"当前蓝量{self.__mp},小于50不能放大招")

    def __init__(self, hp, mp):
        self.__hp = hp
        self.__mp = mp
        print("student类创建了一个对象")


# 创建对象
my_hreo = Hero(100, 49)
my_hreo.dazhao()
