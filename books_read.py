import _locale  ##中文不能正常显示的问题
_locale._getdefaultlocale = (lambda *args: ['zh_CN', 'utf8']) ##中文不能正常显示的问题
##books.txt 是这样写入的  康熙 电子书 书柜    中间是空格
fo1=open("books.txt","r")  ##打开文件
lines=fo1.readlines()  ##把所有内容读入到lines变量内
fo1.close() ##关闭文件
#print(lines[0])  ##第一行  #print(lines[1])  ##第二行
alldata=[]   ##初始化list, 后续要把所有的内容切片,放入alldata 列表内 1行就有3个变量,2行就是6个变量,最后一个是 alldata[5]
for i in range(len(lines)):
    for j in range(3):
        temp=lines[i].split( ) ##行切片,.以空格来切,
        alldata.append(temp[j])

print(alldata," alldata的长度: ",len(alldata))
