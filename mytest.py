"""a=2
b=2.5
c='happy'
d="let's go"
print(a,b,c,d)
#让变量从键盘接收数值
e=input('请输入你的数值:')
print(e)
#未俩个变量输入
f,g=input('请输入你的数值:').split(',')
print(f,g)

#格式化输出
#print('%d','%f','%s')%(d,f,g)


#format输出
#print('a={},b={},c={}'.format(a,b,c))

#练习：定义一个1-9的元组，1、输出倒数第3个元素；2、输出值468
a=[1,2,3,4,5,6,7,8,9]
print(a[-3])
print(a[3:8:2])

#思考：如何定义1-999的元组？
list(range(1,1000))
print(list(range(1,1000)))
"""

s=[1,1,2,3,4,5,6]
a=[7,8,9]
#插入
#s.insert(2,9)
#result = print(s)
#追加
#s.append(7)
#result = print(s)
#链接
#s.extend(a)
#result = print(s)
#删除指定元素
#s.pop(3)
#result = print(s)
#删除指定元素第一次出现的值
#s.remove(1)
#result = print(s)
#9、返回该值在列表中出现的次数
#l=s.count(1)
#result = print(l)
#10、	返回列表中元素最大值
#l=max(s)
#result = print(l)
#11、	返回列表中元素最小值
#l=min(s)
#result = print(l)
#12、	长度,就是yuanzu个数
#l=len(s)
#result = print(l)
#13、删除s[n]，n为下标
#del s[1]
#result = print(s)
#14、	获得元素的下标
#a=s.index(3)
#result = print(a)
#15、清空列表
#a=s.clear()
#result = print(a)