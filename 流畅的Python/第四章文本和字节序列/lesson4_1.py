import array

'''
明确区分了人类可读的文本字符串和原始的字节序列。隐式地把字节序列转换成 Unicode 文本已成过去。本章将要讨论 Unicode 字符
串、二进制序列，以及在二者之间转换时使用的编码。

# 4.1 字符问题
“字符串”是个相当简单的概念：一个字符串是一个字符序列。问题出在“字符”的定义上。
在 2015 年，“字符”的最佳定义是 Unicode 字符

Unicode 标准把字符的标识和具体的字节表述进行了如下的明确区分。字符的标识，即码位，是 0~1 114 111 的数字（十进制），在
Unicode 标准中以 4~6 个十六进制数字表示，而且加前缀“U+”。
    例如，字母 A 的码位是 U+0041，欧元符号的码位是 U+20AC，高音谱号的码位是 U+1D11E。
    在 Unicode 6.3 中（这是 Python 3.4 使用的标准），约 10% 的有效码位有对应的字符。
    字符的具体表述取决于所用的编码。编码是在码位和字节序列之间转换时使用的算法。
        在 UTF-8 编码中，A（U+0041）的码位编码成单个字节 \x41，
        而在 UTF-16LE 编码中编码成两个字节\x41\x00。
        再举个例子，欧元符号（U+20AC）在 UTF-8 编码中是三个字节——\xe2\x82\xac，
        而在 UTF-16LE 中编码成两个字节：\xac\x20。
把码位转换成字节序列的过程是编码；把字节序列转换成码位的过程是解码。示例 4-1 阐释了这一区分。
'''
'''
    ❶ 'café' 字符串有 4 个 Unicode 字符。
    ❷ 使用 UTF-8 把 str 对象编码成 bytes 对象。
    ❸ bytes 字面量以 b 开头。
    ❹ 字节序列 b 有 5 个字节（在 UTF-8 中，“é”的码位编码成两个字节）。
    ❺ 使用 UTF-8 把 bytes 对象解码成 str 对象。

如果想帮助自己记住 .decode() 和 .encode() 的区别，可以把字节序列想成晦涩难懂的机器磁芯转储，把 Unicode 字符串想
成“人类可读”的文本。那么，把字节序列变成人类可读的文本字符串就是解码，而把字符串变成用于存储或传输的字节序列就是编码。

'''
print('示例 4-1　编码和解码', '-' * 20)
s = 'cafe'
print('#1', len(s))  # 1

b = s.encode('utf8')  # 2
print('#3', b)  # 3
print('#4', len(b))  # 4
print('#5', b.decode('utf8'))  # 5

print('\n示例 4-2　包含 5 个字节的 bytes 和 bytearray 对象', '-' * 20)

'''
    ❶ bytes 对象可以从 str 对象使用给定的编码构建。
    ❷ 各个元素是 range(256) 内的整数。
    ❸ bytes 对象的切片还是 bytes 对象，即使是只有一个字节的切片。
    ❹ bytearray 对象没有字面量句法，而是以 bytearray() 和字节序列字面量参数的形式显示。
    ❺ bytearray 对象的切片还是 bytearray 对象。
'''

cafe = bytes('cafe', encoding='utf_8')  # 1
print('#1', cafe)
print('#2', cafe[0])  # 2
print('#3', cafe[:1])  # 3

cafe_arr = bytearray(cafe)
print('#4', cafe_arr)  # 4
print('#5', cafe_arr[-1:])  # 5


'''
➊ 指定类型代码 h，创建一个短整数（16 位）数组。
➋ octets 保存组成 numbers 的字节序列的副本。
➌ 这些是表示那 5 个短整数的 10 个字节。
'''
print('\n示例 4-3　使用数组中的原始数据初始化 bytes 对象', '=' * 20)

numbers = array.array('h', [-2, -1, 0, 1, 2])  # 1
octets = bytes(numbers)  # 2
print(octets)  # 3


'''

'''
print('\n示例 4-4 展示了如何使用 memoryview 和 struct 提取一个 GIF 图像的宽度和高度','='*20)
import struct
fmt = '<3s3sHH'
with open('filter.gif','rb') as fp:
    img = memoryview(fp.read())

header = img[:10]
print(bytes(header))

struct.unpack(fmt,header)

del header
del img


