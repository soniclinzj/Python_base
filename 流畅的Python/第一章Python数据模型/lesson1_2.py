# 1.2 如何使用特殊的方法
# 20190521 Sonic
'''
在 Python 类中有些方法名、属性名的前后都添加了双下画线，这种方法、属性通常都属于 Python 的特殊方法和特殊属性，
开发者可以通过重写这些方法或直接调用这些方法来实现特殊的功能。

最常见的特殊方法就是前面介绍的构造方法：__init__，开发者可以通过重写类中的 __init__ 方法来实现自己的初始化逻辑。

Python 是一门尽量简单的语言，它不像某些语言（如 Java）需要让类实现接口，并实现接口中的方法。
Python 采用的是一种“约定”的机制，Python 按照约定，以特殊名字的方法、属性未提供特殊的功能。

Python 类中的特殊方法、特殊属性有些需要开发者重写，有些则可以直接调用，掌握这些常见的特殊方法、特殊属性也是非常重要的。

'''

"""
Python基础教程，Python入门教程（非常详细）
http://c.biancheng.net/python/
"""



from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r,%r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


v1 = Vector(2, 4)
v2 = Vector(2, 1)
v3 = v1 + v2
print('v3=', v3)

v = Vector(1, 1)

print(abs(v))
print(abs(v3 * 3))


print('1.2.2','==='*10)

print(dir(hypot))