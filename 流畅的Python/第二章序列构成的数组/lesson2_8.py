import bisect
import sys
import random

'''

'''

'''
# 2.8 用bisect来管理已排序的序列
    bisect 模块包含两个主要函数，bisect 和 insort，两个函数都利用
    二分查找算法来在有序序列中查找或插入元素。

    bisect(haystack, needle) 在 haystack（干草垛）里搜索needle（针）的位置，该位置满足的条件是
    ，把 needle 插入这个位置之后，haystack 还能保持升序。也就是在说这个函数返回的位置前面的值，
    都小于或等于 needle 的值。其中 haystack 必须是一个有序的序列。你可以先用 bisect(haystack, needle)
    查找位置 index，再用 haystack.insert(index, needle) 来插入新值。但你也可用
    insort 来一步到位，并且后者的速度更快一些。


        #1 用特定的 bisect 函数来计算元素应该出现的位置。
        #2 利用该位置来算出需要几个分隔符号。
        #3 把元素和其应该出现的位置打印出来。
        #4 根据命令上最后一个参数来选用 bisect 函数。
        #5 把选定的函数在抬头打印出来。

'''


print('\n2.8', '=' * 20)

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'


def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)  # 1
        offset = position * '  |'  # 2
        print(ROW_FMT.format(needle, position, offset))  # 3

        '''
        format()函数
        字符串的参数使用{NUM}进行表示,0, 表示第一个参数,1, 表示第二个参数, 以后顺次递加;
        这里面：{0:2d} 表示第一个参数x的格式。0 代表x,:2d 表示两个宽度的10进制数显示。
               {1:3d} 表示第一个参数x*x的格式。1 代表x*x,:3d 表示三个宽度的10进制数显示。
               {2:4d} 表示第一个参数x*x*x的格式。2代表x*x*x,:4d 表示四个宽度的10进制数显示。

               主要目的是使不同位数的数字排列时，预留出对应的数字占用空间，列排时数字靠右对齐

        '''


print('=' * 20)
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))

print('=' * 20)

if __name__ == '__main__':
    if sys.argv[-1] == 'left':  # 4
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

print('DEMO:', bisect_fn.__name__)  # 5
print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
# Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
demo(bisect_fn)

print('=' * 20)
#Python格式化字符 %s %d %f
# 例：数字格式化
nYear = 2019
nMonth = 5
nDay = 31
# 格式化日期 %02d数字转成两位整型缺位填0
print('%04d-%02d-%02d' % (nYear, nMonth, nDay))
print('=' * 20)

# 示例 2-18　根据一个分数，找到它所对应的成绩


def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]


print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])

print('#2.8.2', '=' * 20)

'''
# 2.8.2 用bisect.insort插入新元素
    insort(seq, item) 把变量 item 插入到序列 seq 中，并能保持 seq的升序顺序。

'''
SIZE = 7
random.seed(1729)
'''
#seed() 用于指定随机数生成时所用算法开始的整数值，
# 如果使用相同的seed(n)值，则每次生成的随即数都相同，
# 如果不设置这个值，则系统根据时间来自己选择这个值，此时每次生成的随机数因时间差异而不同
'''
my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE * 2)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)

# print(help(bisect))