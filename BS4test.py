from bs4 import BeautifulSoup

demo='''
<html><head><title>This is a python demo page</title></head>
<body>
<p class="title"><b>The demo python introduces several python courses.</b></p>
<p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
<a href="http://www.icourse163.org/course/BIT-268001" class="py1" id="link1">Basic Python</a> and <a href="http://www.icourse163.org/course/BIT-1001870001" class="py2" id="link2">Advanced Python</a>.</p>
</body></html>
'''

soup=BeautifulSoup(demo,'html.parser')#解析器类型1.html.parser2.lxml,需要安装：pip install lxml。3. xml安装lxml时就同时带有了。 4.html5lib 需要安装：pip install html5lib

print(soup.title)
print(soup.a.name)
print(soup.a.parent.name)
print(soup.a.attrs)
print(soup.a.attrs["class"])
print(soup.a.attrs["href"])
print(soup.a.string)
##########html内容遍历方法##########
#上行遍历
# parent列表类型
# parents迭代类型
# 下行遍历:
# .contents所有儿子节点，列表类型
# .childern所有儿子节点，迭代类型
# .descendants所有子孙节点迭代类型
# 平行遍历
# .next_sibling列表类型
# .previous_sibling列表类型
# .next_siblings迭代类型
# .previous_siblings迭代类型

##########html内容输出##########
#print(soup.prettify())增加换行符打印

##########utf8是bs4默认编码##########

##########信息标记三种形式##########
# xml:<tag></tag>
# json(有类型键值对):key:value,key:[],key:{key1:value1,key2:value2}
# yaml(无类型键值对，缩进表示递进关系，-表示并列)
# key:value,
# key:#comment
# -value1
# -value2
# key:
#   key1:value1
#   key2:value2

##########信息提取##########