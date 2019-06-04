import sys
import re


'''
UML 科普:
最好是一个团队执行，一个人很难做。每个人负责几个类。对每一个Use case其中的情景。
导引者指定从某一个人的类开始，某一个人看一看自己能够独立完成，如果不能完成，
大家看一看手中的类，谁能完成，就站起来，宣布自己能够完成，以致继续这个过程，
每个人完成自己的职责就坐下。在这过程中不断修改类的责任，并写下协作者的名字。

UML类图入门，看完基本懂了怎么画图了:https://blog.csdn.net/u013870094/article/details/78826614

编程是一门技术，更是一门艺术，不能只满足于写完代码后运行结果正确就完整，时常要考虑如何让代码更加简练，
更加容易维护，容易扩展和利用，只有这样才可以真正得到提高。写出优雅的代码真的是一种很爽的事情。
UML类图也不是一学就会的，需要有一个慢慢熟练的过程。所谓学无止境，其实这才是理解面向对象的开始呢。
'''


'''
# 3.1　泛映射类型
1：collections.abc 中的 MutableMapping 和它的超类的UML 类图（箭头从子类指向超类，抽象类和抽象方法的名称以斜体显示）
然而，非抽象映射类型一般不会直接继承这些抽象基类，它们会直接对dict 或是 collections.User.Dict 进行扩展。这些抽象基类的主要
作用是作为形式化的文档，它们定义了构建一个映射类型所需要的最基本的接口。然后它们还可以跟 isinstance 一起被用来判定某个数据是
不是广义上的映射类型

抽象类与非抽象类，可散列等下阶段进阶版再深入

'''


'''
# 3.2　字典推导

        ❶ 一个承载成对数据的列表，它可以直接用在字典的构造方法中。
        ❷ 这里把配好对的数据左右换了下，国家名是键，区域码是值。
        ❸ 跟上面相反，用区域码作为键，国家名称转换为大写，并且过滤掉区域码大于或等于 66 的地区。

'''

print('3.2', '=' * 20)
print('示例 3-1字典推导的应用', ' . ' * 20)

DIAL_CODES = [  # 1
    (86, 'China'), (91, 'India'), (1, 'United States'), (62, 'Indonesia'),
    (55, 'Brazil'), (92, 'Pakistan'), (880, 'Bangladesh'), (234, 'Nigeria'),
    (7, 'Russia'), (81, 'Japan'),
]
country_code = {country: code for code, country in DIAL_CODES}  # 2
print('#2:  ', country_code)

list_country = {code: country.upper() for country,
                code in country_code.items() if code < 66}  # 3

print('#3:  ', list_country)


'''
3.3　常见的映射方法
表3-1：dict、collections.defaultdict和collections.OrderedDict这三种映射类型的方法列表（依然省略
了继承自object的常见方法）；可选参数以[...]表示

d.clear()                   •   •   •   移除所有元素
d.__contains__(k)           •   •   •   检查 k 是否在 d 中
d.copy()                    •   •   •   浅复制
d.__copy__()                    •       用于支持 copy.copy
d.default_factory               •       在 __missing__ 函数中被调用的函数，用以给未找到的元素设置值*
d.__delitem__(k)            •   •   •   del d[k]，移除键为 k 的元素
d.fromkeys(it,[initial])    •   •   •   将迭代器 it 里的元素设置为映射里的键，如果有 initial 参数，就把它作为这些键对应的值（默认是 None）
d.get(k,[default])          •   •   •   返回键 k 对应的值，如果字典里没有键 k，则返回 None 或者   default
d.__getitem__(k)            •   •   •   让字典 d 能用 d[k] 的形式返回键k 对应的值
d.items()                   •   •   •   返回 d 里所有的键值对
d.__iter__()                •   •   •   获取键的迭代器
d.keys()                    •   •   •   获取所有的键
d.__len__()                 •   •   •   可以用 len(d) 的形式得到字典里键值对的数量
d.__missing__(k)                •       当 __getitem__ 找不到对应键的时候，这个方法会被调用
d.move_to_end(k,[last])             •   把键为 k 的元素移动到最靠前或者最靠后的位置（last 的默认值是 True）
d.pop(k, [defaul]           •   •   •   返回键 k 所对应的值，然后移除这个键值对。如果没有这个键，返回 None 或者 defaul
d.popitem()                 •   •   •   随机返回一个键值对并从字典里移除它#
d.__reversed__()                    •   返回倒序的键的迭代器
d.setdefault(k,[default])   •   •   •   若字典里有键k，则把它对应的值设置为 default，然后返回这个值；若无，则让 d[k] =default，然后返回 default
d.__setitem__(k,v)          •   •   •   实现 d[k] = v 操作，把 k 对应的值设为v
d.update(m,[**kargs])       •   •   •   m 可以是映射或者键值对迭代器，用来更新 d 里对应的条目
d.values()                  •   •   •   返回字典里的所有值

上面的表格中，update 方法处理参数 m 的方式，是典型的“鸭子类型”。函数首先检查 m 是否有 keys 方法，如果有，那么 update 函数就
把它当作映射对象来处理。否则，函数会退一步，转而把 m 当作包含了键值对 (key, value) 元素的迭代器。Python 里大多数映射类型的构造
方法都采用了类似的逻辑，因此你既可以用一个映射对象来新建一个映射对象，也可以用包含 (key, value) 元素的可迭代对象来初始化一个
映射对象。
在映射对象的方法里，setdefault 可能是比较微妙的一个。我们虽然并不会每次都用它，但是一旦它发挥作用，就可以节省不少次键查询，
从而让程序更高效。如果你对它还不熟悉，下面我会通过一个实例来讲解它的用法。
'''

print('示例 3-2 这段程序从索引中获取单词出现的频率信息，并把它们写进对应的列表里', '\n', ' . ' * 20)

'''
❶ 提取 word 出现的情况，如果还没有它的记录，返回 []。
❷ 把单词新出现的位置添加到列表的后面。
❸ 把新的列表放回字典中，这又牵扯到一次查询操作。
❹ sorted 函数的 key= 参数没有调用 str.uppper，而是把这个方法的引用传递给 sorted 函数，这样在排序的时候，单词会被规范成统一格式。
'''

"""
#创建一个从单词到其出现情况的映射-- index0.py

WORD_RE = re.compile(r'\w+')
index = {}

with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            # 这其实是一种很不好的实现，这样写只是为了证明论点
            occurrences = index.get(word, [])  # ➊
            occurrences.append(location)  # ➋
            index[word] = occurrences  # ➌
            # 以字母顺序打印出结果
for word in sorted(index, key=str.upper):  # ➍
    print(word, index[word])    
    
于 Terminal 下执行 python3 index0.py zen.txt

"""

print('3.8', '=' * 20)
'''
# 3.8 集合论
“集”这个概念在 Python 中算是比较年轻的，同时它的使用率也比较低。
本书中“集”或者“集合”既指 set，也指 frozenset。
'''
l = ['spam', 'spam', 'eggs', 'spam']
print(set(l))
print(list(set(l)))
print(type(l))

s = {1}
print(type(s))
print(s)

print(s.pop())
print(s)

from dis import dis
print(dis('{1}'))
print(dis('set[1]'))

from unicodedata import name
codes = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i),'')}
print(codes)

'''这节有点深奥难懂，需加视频再复习'''