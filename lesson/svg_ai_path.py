
import json
'''

f = open("lesson_ai_path.svg",'r',encoding="utf_8")# 以只读方式打开,加上编码不会产生乱码

s=f.read()

path_rule_start = '<path d="'
path_rule_end = 'z"/>'

open('path_aaa1.txt','a+',encoding='utf_8')

for k in s:
    print(k)

------------------
f = open("lesson_ai_path.svg",'r',encoding="utf_8")# 以只读方式打开,加上编码不会产生乱码

svg_paths=f.read()

path_start = '<path d="'
path_end = 'z"/>'


def get_str_btw(s, f, b):
    par = svg_paths.partition(f)
    return (par[2].partition(b))[0][:]


svg_path = open('path_aaa1.txt','a+',encoding='utf_8')
tmp = get_str_btw(svg_paths,path_start,path_end)
print(tmp)

svg_path.wirte(tmp)

'''
'''
data = []
for line in open("lesson_ai_path.svg","r"): #设置文件对象并读取每一行文件
    data.append(line)               #将每一行文件加入到list中

for k in data:
    print('\n',k)
'''

f = open("lesson_ai_path.svg",'r',encoding="utf_8")# 以只读方式打开,加上编码不会产生乱码
svg_paths=f.read()
path_start = '<path d="'
path_end = '</svg>'

#获取两个字符之间的内容：
def get_str_btw(s, f, b):
    par = s.partition(f)
    return (par[2].partition(b))[0][:]

svg_path = open('path_aaa.txt','w',encoding='utf_8')
svg_path_1 = open('path_bbb.txt','w',encoding='utf_8')

tmp = get_str_btw(svg_paths,path_start,path_end)

tmp1=tmp.replace('"/>','').replace(path_start,'')# 查找并替换

svg_path.write(tmp1) #写入文件
data = []
data = tmp1.split(' ')# 依空格进行数据封装

svg_path_1.write(str(data))

print(data)


print('\n例二','*'*20)


ff = open("info.txt")
line = ff.readline()
while line:
    #dump将字符串转换成字典
    d1=json.loads(line)
    print (type(d1))
    print (d1['item_id'])
    line = ff.readline()

ff.close()
