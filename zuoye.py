# 练习：分别定义一个集合和一个字典
'''
#集合
s={1,2,4}
#字典
d={'name':'wyh','age':'18'}
'''
# 1-	为集合和字典分别插入元素：55（d：55）
'''
#集合
s={1,2,4}
s.add(3)#添加元素
print(s)
#字典
d={'name':'wyh','age':'18'}
d['aihao'] = 'dota'#添加键值对
print(d)
'''

# 2-	分别删除集合和字典内的一个元素
'''
#集合
s={1,2,4}
s.remove(4)
print(s)
#字典
d={'name':'wyh','age':'18'}
del d['age']
print(d)
'''
# 3-	取出字典内的所有值（value）和集合组合一个列表(这个重点是要将字典和集合都强制转换成列表)
'''
#集合
s={1,2,4}
s1=list(s)
#字典
d={'name':'wyh','age':'18'}
biao=list(d.values())
s1.extend(biao)
print(s1)
'''

# 4-集合和字典的区别
'''
①创建空集合：set() 创建空字典 {}
②集合不可重复，无序 字典键不可重复，无序
'''
#分支判断
#1、if练习--从键盘输入一个数，判断该数是否在列表中，如果在就打印happy
'''
# a=int(input('请输入一个数字：'));
# l=[1,2,3];
# if a in l:
#     print('恭喜你答对了：','happy');
'''
#2-	if-else练习—从键盘输入一个数，判断该数是否在列表中，如果在就打印happy，并且让列表中的该值+1，否则打印sad
'''
# a=int(input("请输入一个数字："))
# m=[1,2,3,4,5,6,7]
# if a in m:
#     print('happy')
#     b=m.index(a)
#     print(b)
#     m[b]=m[b]+1
#
# else:
#     print('sad')
# print(m)
'''
# 3-	输入一个数，判断该数的范围：90-100：等价为A……60以下：等级为E
'''
# a=int(input('请输入一个数字：'))
# if 90<=a<=100:
#     print('等级为A')
# elif 80<=a<90:
#     print('等级为B')
# elif 70<=a<80:
#     print('等级为C')
# elif 60<=a<70:
#     print('等级为D')
# elif a<60:
#     print('等级为E')
'''

# 设计一个计算器，输入两个数，自动实现加减乘除
'''
# def he(a,b):
#     print(a+b)
# def cha(a,b):
#     print(a-b)
# def ji(a,b):
#     print(a*b)
# def shang(a,b):
#     print(a/b)
# he(1,2)
# cha(1,2)
# ji(1,2)
# shang(1,2)
'''
# （进阶：根据用户输入的计算符号计算结果）
'''
# def he(a,b):
#     print(a+b)
# def cha(a,b):
#     print(a-b)
# def ji(a,b):
#     print(a*b)
# def shang(a,b):
#     print(a/b)
# a=int(input('请输入第一个数字：'))
# b=int(input('请输入第二个数字：'))
# c=input('请输入运算符：')
# if c=='+':
#     he(a,b)
# if c=='-':
#     cha(a,b)
# if c=='*':
#     ji(1, 2)
# if c=='/':
#     shang(a,b)
'''
# 计算1+2+3+4……+100的和
'''
# a=1
# b=0
# while a<=100:
#     b=b+a
#     a=a+1
# print(b)
'''
# 求10阶乘
'''
# a=1
# ji=1
# while a<=10:
#     ji=a*ji
#     a=a+1
# print(ji)
'''

# 求100以内能被3整除的数，并将作为列表输出
'''
biao =[]
for a in range(1,101):
    if a%3==0:
        #print(a)
        biao.append(a)#在列表中把这个值加入进去
print(biao)
'''

# 列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表
'''
a=[1,2,3,4,3,4,2,5,5,8,9,7]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)
'''

# 求斐波那契数列 1 1 2 3 5 8 13 ……
'''
a=0
b=1
c=0
for i in range(1,6):
    c=a+b #前俩个数相加等于第三个（3个为1组）
    b=a#然后对于第2组数来说b就是a
    a=c#对于第四个数来说c就是b
    print(c)
'''
# 求100以内的质数（只能被1和它本身整除）:只能被1和本身整除代表不能被其他数整除
"""
for a in range(1,101):
    biao=[]
    for b in range(1,101):
        if a%b==0:
            # print(b)#(如果a%b==0，那么打印出b，看看a能被几个数整除)
            biao.append(b)#(如果a能被超过2个数（既是b）整除，那么就不是质数)
    # print(biao)#将所有可以整除a的b放在列表中；在下一步中，如果列表长度等于2说明就是质数
    if len(biao)==2:
        print(a,'该数是质数')
    # else: 
    #     print('该数不是质数')
"""

# 读取data文件中的数据，将所有的数字去重并按照从小到大的顺序写入backup文件
'''
biao=[]
with open('D:\lx2.txt','r') as f:
    a=f.read().splitlines()
    print(a)
for b in a:
    c = b.split(',')
    print(b.split(','))
    for d in c:
        e = int(d)
        print(e)
        if e not in biao:
            biao.append(e)
print(biao)
q=sorted(biao)
print(q)

with open('D:\lx3.txt','w+') as m:
    for i in q:
        n=str(i)
        m.write(n)
        m.write(',')
'''
# 练习1：读取以下文件：a-全部内容；b-每一行的内容；c-读取所有行的内容
'''
# 全部
f = open('D:/lx.txt','r')
print(f.read())
f.close()
每一行
a=1
f = open('D:/lx.txt','r')
while 1<=a<=6:
    print(f.readline())
    a=a+1
f.close()
# 每一行
f=open('D:/lx.txt','r')
for a in range(1,7):
    print(f.readline())
f.close()
# 读取所有行
f = open('D:/lx.txt', 'r')
print(f.readlines())
f.close()
'''
"""
不需要写f.close()的方法
with open('D:/lx.txt','r') as f:
    contnet=f.read()
    print(contnet)
"""
# 练习2：读取以下文件的全部内容，并将所有的数字去重后，放入一个列表
'''
biao=[]
with open('D:/lx2.txt','r') as f:
    a=f.read().splitlines()
    print(a)
for b in a:
    #print(b.split(','))
    for c in b.split(','):
        d=int(c)
        #print(d)
        if d not in biao:#去重
            biao.append(d)
print(biao)
'''
# 练习3：将以上文件的全部内容写入一个新的文件，并按照从小到大的顺序
'''
biao=[]
with open('D:\lx2.txt','r') as f:
    a=f.read().splitlines()
    print(a)
for b in a:
    c = b.split(',')
    print(b.split(','))
    for d in c:
        e = int(d)
        print(e)
        biao.append(e)
print(biao)
q=sorted(biao)
print(q)

with open('D:\lx4.txt','w+') as m:
    for i in q:
        n=str(i)
        m.write(n)
        m.write(',')

'''

