# 1、打印小猫爱吃鱼，小猫要喝水
'''
class Cat(object):
    def eat(self):
        print('小猫爱吃鱼')
    def drink(self):
        print('小猫要喝水')
a=Cat()
a.eat()
a.drink()
'''
# 2、小明爱跑步，爱吃东西。
# 1）小明体重75.0公斤
# 2）每次跑步会减肥0.5公斤
# 3）每次吃东西体重会增加1公斤
# 4）小美的体重是45.0公斤
# '''
class Person(object):
    def __init__(self,name,tizhong):
        self.name=name
        self.tizhong=tizhong
    def run(self):
        print(self.name,'跑步')
        self.tizhong=self.tizhong-0.5
    def eat(self):
        print(self.tizhong,'')
        self.tizhong=self.tizhong+1

# '''
# 3、摆放家具
# 需求：
# 1）.房子有户型，总面积和家具名称列表
#    新房子没有任何的家具
# 2）.家具有名字和占地面积，其中
#    床：占4平米
#    衣柜：占2平面
#    餐桌：占1.5平米
# 3）.将以上三件家具添加到房子中
# 4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表
'''
class house(object):
    zongmianji='120'
    shengyumianji='1'
    huxing='三室一厅'
    def baifang(self):
        print()
class jiaju(object):
    chuang='4平米'
    yigui='2平米'
    canzhuomianji='1.5平米'
'''
# 4.士兵开枪
# 需求：
# 1）.士兵瑞恩有一把AK47
# 2）.士兵可以开火(士兵开火扣动的是扳机)
# 3）.枪 能够 发射子弹(把子弹发射出去)
# 4）.枪 能够 装填子弹 --增加子弹的数量
'''
class shibing(object):
    name='瑞恩'
    def kaihuo(self):
        print()
class qiang(object):
    name='ak47'
    def fashe(self):
        print()
    def zhuangtian(self):
        print()
'''