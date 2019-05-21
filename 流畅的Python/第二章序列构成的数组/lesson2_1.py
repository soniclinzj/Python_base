# 2.1 内置序列类型概览
'''
序列类型
        1.容器序列
        list、tuple、collections.deque 这些序列能存放不同类型的数据。

        2.扁平序列
        str、bytes、bytearray、memoryview 和array.array 这类序列只能容纳一种类型，即一段连续的内存空间只能存放一些基础类型如字符、字节和数值。

也可按能否修改进行分类:
        1.可变序列（MutableSequence）
        list、bytearray、array.array、collections.deque 和 memoryview.
        2.不可变序列(Sequence)
        tuple、str 和 bytes
'''

# 2.2 列表推导和生成器表达式
'''
列表推导是构建列表（list）的快捷方式，而生成器表达式则可以用来创建其它任何类型的序列。
很多程序员将列表推导（list comprehension）简称为listcomps,生成器表达式（generator expression）则称为genexps。

通常原则，只用列表推导来创建新的列表并且尽量保持简短。如果代码超过两行，就要考虑是否要用for循环重写。
'''

x = "林志坚"
y = 'I love you !'

dummy = [ord(k) for k in y]
print(dummy)

dummy = [ord(k) for k in x]
print(dummy)


print('2.2.3', ' = ' * 10)

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]

print(tshirts)


for color in colors:
    for size in sizes:
        print((color, size))

tshirts = [(color, size) for size in sizes for color in colors]

print(tshirts)

# 2.2.4 生成器表达式
'''
生成器表达式背后遵守了迭代器协议，可以逐个的产出元素，而不是先建立一个完整的列表，然后再把这个列表传递到某个构造函数里。
生成器表达式的语法与列表推导差不多，只不过是把方括号换成圆括号而已。
'''
print('2.2.4', '=' * 20)

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)
'''
生成器表达式会在每次for循环运行时才生成一个组合，不会在内存里留下一个有6个组合的列表，如果要计算各有1000个元素的笛卡儿积，
生成器表达式就可以帮忙省掉运行for循环的开销，即一个含有100万个元素的列表。
生成器表达式逐个产出元素，从来不会一次性产出一个完整的列表。
'''
