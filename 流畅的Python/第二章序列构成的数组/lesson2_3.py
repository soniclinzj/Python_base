# 元组不仅仅是不可变的列表
import os
from collections import namedtuple

'''
元组其实是对数据的记录：元组中的每个元素都存放了记录中一个字段的数据，外加这个字段的位置。正是这个位置信息给数据赋予了意义。
把元组当作一些字段的集合，那么数量和位置信息就变的非常重要了。
        元组()
        列表[]

'''

# 把元组用作记录
'''
#1 洛杉矶国际机场的经纬度
#2 东京市的一些信息：（市名、年份、人口、人口变化和面积）
#3 一个元组列表，元组的形式为(country_code,passport_number)
#4 在迭代的过程中，passport 变量被绑定到每个元组上
#5 %格式运算符能被匹配到对应的元组元素上
#6 for 循环可以为别提取元组里的元素，也叫作拆包（unpacking）。因为元组中第二个元素对我们没有什么用，所以它赋值给"_"占位符。
#7 最好辨认的元组拆包形式就是平行赋值
#8 不使用中间变量交换两个变量的值
#9 用 * 运算符把一个可迭代对象拆开作为函数的参数。
#10 拆包时我们不总是对元组里所有的数据都感兴趣，_占位符能帮助处理这种情况.
#11 在平行赋值中，*前缀只能用在一个变量名前面，但是这个变量可以出现在赋值表达式的任意位置

'''

print('2.3.1', '==' * 20)

lax_coordinates = (33.9425, -118.408056)  # 1
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)  # 2
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'),
                ('ESP', 'XDA205856')]  # 3
for passport in sorted(traveler_ids):  # 4
    print('%s/%s' % passport)  # 5

for country, _ in traveler_ids:  # 6
    print(country)


latitude, longitude = lax_coordinates  # 7

print(latitude, longitude)


a = 1
b = 2
b, a = a, b  # 8
print(a, b)


# python divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。

divmod(20, 8)
t = (20, 8)
print(divmod(*t))

quotient, remainder = divmod(*t)  # 9
print(quotient, remainder)


# os.path.split()函数会返回以路径和最后一个文件名组成的元组（path,last_part）

_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')  # 10
print(filename)

path, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
print(path)
print(filename)


a, b, *rest = range(10)  # 11
print(a, b, rest)

a, b, *rest = range(2)
print(a, b, rest)

*a, b, rest = range(5)
print(a, b, rest)


print('\n2.3.3', '==' * 20)

'''
表达式的元组可以是嵌套式的，例如（a,b,(c,d)）只要这个接受元组的嵌套结构符合表达式本身的嵌套结构。
#1 每个元组内有4个元素，其中最后一个元素是座标。
#2 把输入元组的全部对应进行拆包，不用的可用项目可用"_"进行忽略，这样最后一个元素拆包到由变量构成的元组里，这样就获取了座标
#3 if longitude <=0 这个条件判断把输出限制在西半球的城市
'''
metor_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),  # 1
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

print('{:15}|{:^9}|{:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15}|{:9.4f}|{:9.4f}'
for name, cc, pop, (latitude, longitude) in metor_areas:  # 2
    if longitude <= 0:  # 3
        print(fmt.format(name, latitude, longitude))


print('\n2.3.4', '==' * 20)

# 定义和使用具名元组
'''
#1 创建一个具名元组需要两个参数，一个是类名，别一个是类的各个字段的名字。后者可以是由数个字符串组成的可迭代的对象，或者是由空
    格分隔开的字段名组成的字符串。
#2 存放在对应字段里的数据要以一串参数的形式传入到构造函数串（注意，元组的构造函数却只接受单一的可迭代对象）
#3 可以通过字段名或者位置来获取一个字段的信息
'''

City = namedtuple('City', 'name country population coordinates')  # 1
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))  # 2

print(tokyo)  # 3

print(tokyo.population)  # 3

print(tokyo.coordinates)  # 3

print(tokyo[0])  # 3


# 元组的属性和方法
'''
#4 _fields 属性是一个包含这个类所有字段名称的元组
#5 用_make()通过接受一个可迭代对象来生成这个类的一个实例，它的作用跟City(*delhi_data)是一样的。
#6 _asdict()把具名元组以collections.OrderedDict 的形式返回，我们可以利用它把元组里的信息友好的呈现出来。
'''
c = City._fields  # 4
print('#4 c:\n',c)

LatLong = namedtuple('LatLong', 'lat long')

delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))

delhi = City._make(delhi_data)  # 5
print('#5 delhi:\n',delhi)

d = delhi._asdict()  # 6
print('#6 d:\n',d)

for k,v in delhi._asdict().items():
    print(k+':',v)


# 元组是一种很强大的可以当作记录来用的数据类型。它的第二个角色则是充当一个不可变的列表。
'''
如果把元组当列表来用，它们的相似度：除了增减元素相关方法之外，元组没有__reversed__

方法或属性             列表    元组        含义
s.__add__(s2)         有      有         s+s2 
s.__iadd__(s2)        有      无         s+=s2  
s.apppend(e)          有      无          尾部新加一个元素
s.clear()             有      无         删除所有元素
s.__contains__(e)     有      有         s是否包含了e
s.copy()              有      无         列表的浅拷贝
s.count(e)            有      有         e在s中出现的次数
s.__delitem__(p)      有      无         把位于p的元素删除了
s.extend(it)          有      无         把可迭代的对象it追加个s
s.__getnewargs__()    无      有         在pickle中支持更加优化的序列化
s.index(e)            有      有         在s中找到元素e第一次出现的位置
s.insert(p,e)         有      无         在位置p之前插入元素e
s.__iter__()          有      有         获取s的迭代器
s.__len__()           有      有         len(s)元素的数量
s.__mul__(n)          有      有         s*n，n个s重复拼接
s.__imul__(n)         有      无         就地n次拼接
s.__rmul__(n)         有      有         n*s，反向拼接
s.pop([p])            有      无         删除最后一个，或者指定p位置的元素。可选p
s.remove(e)           有      无         删除s中第一次出现的e
s.reverse()           有      无         原地把s的元素倒序排列
s.__reversed__()      有      无         返回s的倒序迭代器
s.__setitem__(p,e)    有      无         s[p]=e，把元素放在位置p上，替代原来的那个位置
s.sort([key],[reverse]) 有    无         就地对s中元素进行排序。可选key或是否倒序reverse
'''