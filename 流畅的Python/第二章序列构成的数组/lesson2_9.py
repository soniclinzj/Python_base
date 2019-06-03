
'''
# 2.9当列表不是首选时
            虽然列表既灵活又简单，但面对各类需求时，我们可能会有更好的选择。
            比如，要存放 1000 万个浮点数的话，数组（array）的效率要高得多，
            因为数组在背后存的并不是 float 对象，而是数字的机器翻译，也就
            是字节表述。这一点就跟 C 语言中的数组一样。再比如说，如果需要
            频繁对序列做先进先出的操作，deque（双端队列）的速度应该会更快。

            如果在你的代码里，包含操作（比如检查一个元素是否出现在一个集合中）的频率很高，用 set（集合）会更合适。
            set 专为检查元素是否存在做过优化。但是它并不是序列，因为 set 是无序的。


# 2.9.1 数组

            如果我们需要一个只包含数字的列表，那么 array.array 比 list 更高效。数组支持所有跟可变序列有关的操作，
            包括 .pop、.insert 和.extend。另外，数组还提供从文件读取和存入文件的更快的方法，如.frombytes 和 .tofile。

            创建数组需要一个类型码，这个类型码用来表示在底层的 C 语言应该存放怎样的数据类型。比如 b 类型码代表的是有符号
            的字符（signed char），因此 array('b') 创建出的数组就只能存放一个字节大小的整数，范围从 -128 到 127，这样
            在序列很大的时候，我们能节省很多空间。而且 Python 不会允许你在数组里存放除指定类型之外的数据。


                # 1 引入 array 类型。
                # 2 利用一个可迭代对象来建立一个双精度浮点数组（类型码是 'd'），这里我们用的可迭代对象是一个生成器表达式。
                # 3 查看数组的最后一个元素。
                # 4 把数组存入一个二进制文件里。
                # 5 新建一个双精度浮点空数组。
                # 6 把 1000 万个浮点数从二进制文件里读取出来。
                # 7 查看新数组的最后一个元素。
                # 8 检查两个数组的内容是不是完全一样。

'''

# 示例 2-20　一个浮点型数组的创建、存入文件和从文件读取的过程

from array import array  # 1
from random import random
import numpy
import string

floats = array('d', (random() for i in range(10**6)))  # 2
print(floats[-1])  # 3

fp = open('floats.bin', 'wb')
floats.tofile(fp)  # 4
fp.close()
floats2 = array('d')  # 5
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**6)  # 6
fp.close()
print(floats2[-1])  # 7

print(floats2 == floats)  # 8

'''
                        列  数
                        表  组
s.__add(s2)__           •   •     s + s2，拼接
s.__iadd(s2)__          •   •     s += s2，就地拼接
s.append(e)             •   •     在尾部添加一个元素
s.byteswap                  •     翻转数组内每个元素的字节序列，转换字节序
s.clear()               •         删除所有元素
s.__contains__(e)       •   •     s 是否含有 e
s.copy()                •         对列表浅复制
s.__copy__()                •     对 copy.copy 的支持
s.count(e)              •   •     s 中 e 出现的次数
s.__deepcopy__()        •         对 copy.deepcopy 的支持
s.__delitem__(p)        •   •     删除位置 p 的元素
s.extend(it)            •   •     将可迭代对象 it 里的元素添加到尾部
s.frombytes(b)              •     将压缩成机器值的字节序列读出来添加到尾部
s.fromfile(f, n)            •     将二进制文件 f 内含有机器值读出来添加到尾部，最多添加 n 项
s.fromlist(l)               •     将列表里的元素添加到尾部，如果其中任何一个元素导致了 TypeError 异常，那么所有的添加都会取消
s.__getitem__(p)        •   •     s[p]，读取位置 p 的元素
s.index(e)              •   •     找到 e 在序列中第一次出现的位置
s.insert(p, e)          •   •     在位于 p 的元素之前插入元素 e
s.itemsize                  •     数组中每个元素的长度是几个字节
s.__iter__()            •   •     返回迭代器
s.__len__()             •   •     len(s)，序列的长度
s.__mul__(n)            •   •     s * n，重复拼接
s.__imul__(n)           •   •     s *= n，就地重复拼接
s.__rmul__(n)           •   •     n * s，反向重复拼接*
s.pop([p])              •   •     删除位于 p 的值并返回这个值，p 的默认值是最后一个元素的位置
s.remove(e)             •   •     删除序列里第一次出现的 e 元素
s.reverse()             •   •     就地调转序列中元素的位置
s.__reversed__()        •         返回一个从尾部开始扫描元素的迭代器
s.__setitem__(p,e)      •   •     s[p] = e，把位于 p 位置的元素替换成 e
s.sort([key],[revers])  •         就地排序序列，可选参数有 key 和 reverse
s.tobytes()                 •     把所有元素的机器值用 bytes 对象的形式返回
s.tofile(f)                 •     把所有元素以机器值的形式写入一个文件
s.tolist()                  •     把数组转换成列表，列表里的元素类型是数字对象
s.typecode                  •     返回只有一个字符的字符串，代表数组元素在 C 语言中的类型

'''

'''
# 2.9.2 内存视图
memoryview 是一个内置类，它能让用户在不复制内容的情况下操作同一个数组的不同切片
        ❶ 利用含有 5 个短整型有符号整数的数组（类型码是 'h'）创建一个memoryview。
        ❷ memv 里的 5 个元素跟数组里的没有区别。
        ❸ 创建一个 memv_oct，这一次是把 memv 里的内容转换成 'B' 类型，也就是无符号字符。
        ❹ 以列表的形式查看 memv_oct 的内容。
        ❺ 把位于位置 5 的字节赋值成 4。
        ❻ 因为我们把占 2 个字节的整数的高位字节改成了 4，所以这个有符号整数的值就变成了 1024。


'''
# memoryview 是一个内置类，它能让用户在不复制内容的情况下操作同一个数组的不同切片
print('#2.9.2', '=' * 20)
numbers = array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)  # 1

print('#1-1', memoryview(numbers))
print('#1-1', memoryview(memv))

print('#1-2', memv.tolist())

print(len(memv))
print('#2', memv[0])  # 2

memv_oct = memv.cast('B')  # 3

print('#4', memv_oct.tolist())  # 4

memv_oct[5] = 4  # 5

print('#6', numbers)  # 6


'''
import array
# array模块是python中实现的一种高效的数组存储类型。它和list相似，但是所有的数组成员必须是同一种类型，在创建数组的时候，就确定了数组的类型
# array.array(typecode,[initializer])
# --typecode:元素类型代码；initializer:初始化器，若数组为空，则省略初始化器
arr = array.array('i',[0,1,1,3])
print(arr)
'''
'''
# 2.9.3 　NumPy和SciPy
        ❶ 安装 NumPy 之后，导入它（NumPy 并不是 Python 标准库的一部分）。
        ❷ 新建一个 0~11 的整数的 numpy.ndarry，然后把它打印出来。
        ❸ 看看数组的维度，它是一个一维的、有 12 个元素的数组。
        ❹ 把数组变成二维的，然后把它打印出来看看。
        ❺ 打印出第 2 行。
        ❻ 打印第 2 行第 1 列的元素。
        ❼ 把第 1 列打印出来。
        ❽ 把行和列交换，就得到了一个新数组。


'''
# 2-22　对 numpy.ndarray 的行和列进行基本操作
print('#2.9.3', '=' * 20)


a = numpy.arange(12)  # 2
print('#2-1', a)
print('#2-2', type(a))
print('#3', a.shape)  # 3

a.shape = 3, 4  # 4  ；3 == 行，4==列
print('#4-1\n',a)
print('#4-2',a.shape)

print('#5',a[2])  # 5

print('#6',a[2, 1])  # 6

print('#7',a[:, 1])  # 7

print('#8\n',a.transpose())  # 8


print('#2.9.3', '=' * 20)

'''
❶ 从文本文件里读取 1000 万个浮点数。
❷ 利用序列切片来读取其中的最后 3 个数。
❸ 把数组里的每个数都乘以 0.5，然后再看看最后 3 个数。
❹ 导入精度和性能都比较高的计时器（Python 3.3 及更新的版本中都有这个库）。
❺ 把每个元素都除以 3，可以看到处理 1000 万个浮点数所需的时间还不足 40 毫秒。
❻ 把数组存入后缀为 .npy 的二进制文件。
❼ 将上面的数据导入到另外一个数组里，这次 load 方法利用了一种叫作内存映射的机制，它让我们在内存不足的情况下仍然可以对数组做切片。
❽ 把数组里每个数乘以 6 之后，再检视一下数组的最后 3 个数。

'''



if False :  # 生成浮点文件
    f = open("floats-10M-lines.txt","a+")
    for k in range(10**4):
        num = str(random()*100000) + '\n'
        f.write(num)

floats = numpy.loadtxt('floats-10M-lines.txt')#1
print('#2',floats[-3:])#2

floats *= .5#3
print('#3',floats[-3:])

from time import perf_counter as pc#4

t0 = pc()
floats /= 3
print('#5-1',pc() - t0)#5
'''
perf_counter() 
    # 调用一次 perf_counter()，从计算机系统里随机选一个时间点A，计算其距离当前时间点B1有多少秒。
    当第二次调用该函数时，默认从第一次调用的时间点A算起，距离当前时间点B2有多少秒。
    两个函数取差，即实现从时间点B1到B2的计时功能。
'''
print('#5-2',floats[-3:])

numpy.save('floats-10M', floats)#6
floats2 = numpy.load('floats-10M.npy', 'r+')#7

floats2 *= 6
print('#8',floats2[-3:])#8