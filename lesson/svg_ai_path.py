
'''

f = open("lesson_ai_path.svg",'r',encoding="utf_8")# 以只读方式打开,加上编码不会产生乱码

s=f.read()

path_rule_start = '<path d="'
path_rule_end = 'z"/>'

open('path_aaa.txt','a+',encoding='utf_8')

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


svg_path = open('path_aaa.txt','a+',encoding='utf_8')
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
path_end = '"/>'


def get_str_btw(s, f, b):
    par = svg_paths.partition(f)
    return (par[2].partition(b))[0][:]

data=[]

svg_path = open('path_aaa.txt','a+',encoding='utf_8')

tmp = get_str_btw(svg_paths,path_start,path_end)
data.append(tmp)

print(data)
