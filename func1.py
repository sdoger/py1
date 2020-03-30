def pi(n):  #π=4*（1-1/3+1/5-1/7+1/9……） 求PI
    s=0
    for i in range(n):
        if i%2==1:
            s=s-1.0/(1+2*i)
        else:
            s=s+1.0/(1+2*i)
    return s*4

def datetime():
    import time
    d1=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return d1

def ss(s1,s2,s3=0,h=0):  ##圆面积
    import math
    ss9=0
    if s1=="y":  ##圆
        ss9=math.pi*s2*s2
    elif s1=="z":   ##正方形
        ss9=s2*s2
    elif s1=='c':  ##长方形
        ss9=s2*s3
    elif s1=="s":  ##三角形
        ss9=s2*s3/2
    elif s1=="t":  ##梯形
        ss9=(s2+s3)*h/2
    return ss9

def cfkjb():  ##乘法口诀表(直接打印出来)
    import time
    for i in range(1,10):  ##<>10
        for j in range(1,i+1):
            print("%d * %d = %d  "%(j,i,i*j),end="")
        print("")
        time.sleep(0.5)

def pailie3(list1):  ##排列 3位数
    a=0
    for i in list1:
        for j in list1:
            for k in list1:
                if( i != k ) and (i != j) and (j != k):
                    a+=1
                    print(i,j,k," ",end="")
    print("\nAll numbers is %d"%(a))

def get_week_day(date):
    import time,datetime
    week_day_dict = {
    0 : '星期一',
    1 : '星期二',
    2 : '星期三',
    3 : '星期四',
    4 : '星期五',
    5 : '星期六',
    6 : '星期天',
    }
    day = date.weekday()
    return week_day_dict[day]

def shuixianhua():   ##题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
##程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。
    for n in range(100,1000):
        i = int(n / 100)
        j = int(n / 10) % 10
        k = n % 10
        if n == i ** 3 + j ** 3 + k ** 3:
            print(n,end=" ")

from ftplib import FTP  ##ftp自定义函数
def upload(f, remote_path, local_path):
    fp = open(local_path, "rb")
    buf_size = 1024
    f.storbinary("STOR {}".format(remote_path), fp, buf_size)
    fp.close()
def download(f, remote_path, local_path):
    fp = open(local_path, "wb")
    buf_size = 1024
    f.retrbinary('RETR {}'.format(remote_path), fp.write, buf_size)
    fp.close()
    if __name__ == "__main__":
        username="pi"
        password="raspberry1"
        ftp = FTP()
        #ftp.set_debuglevel(2)             #打开调试级别2，显示详细信息
        ftp.connect("192.168.**.**", 21)      # 第一个参数可以是ftp服务器的ip或者域名，第二个参数为ftp服务器的连接端口，默认为21
        ftp.login(username, password)     # 匿名登录直接使用ftp.login()
        #ftp.cwd("tmp")                # 切换到tmp目录
        upload(ftp, upfile, upfile)   # 将当前目录下的a.txt文件上传到ftp服务器的tmp目录，命名为ftp_a.txt
        #download(ftp, "ftp_a.txt", "b.txt")  # 将ftp服务器tmp目录下的ftp_a.txt文件下载到当前目录，命名为b.txt
        ftp.quit()

##mysql CHAT
def get_message(sqlip,sqluser,sqlpass,sqldb,user1,towho1,zt1):
    import MySQLdb
    port1=3309
    db = MySQLdb.connect(sqlip, sqluser, sqlpass, sqldb, charset='utf8',port=port1)
    cursor = db.cursor()
    #sql = "SELECT * FROM chat where user='Steven' and zt='1'"
    sql = "SELECT * FROM chat where user="+"'"+user1+"' and towho=" +"'"+towho1+"' and zt='1'"
    #执行sql语句
    cursor.execute(sql)
    results = cursor.fetchall()
    #SQL语句更新数据
    sql = "UPDATE chat SET zt = 2 WHERE user="+"'"+user1+"' and towho=" +"'"+towho1+"'"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print("======================================================================")

    except Exception as e:
        print("数据更新出错：case%s"%e)
        #发生错误是回滚
        db.rollback()
    db.close()
    return results

def send_message(sqlip,sqluser,sqlpass,sqldb,user1,towho1,message1):   ##sql send_message from user1 to towho1, ex. send_message("Steven","czr","Hello")
    import MySQLdb,datetime,time
    #sqlip='xxx.xxx.xxx.xxx'
    #sqlport=3309
    #sqldb='xxx'
    #sqluser='root'
    #sqlpass='xxxx'
    #user1="sender name"
    #towho1="receive name"
    nowtime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    port1=3309
    db = MySQLdb.connect(sqlip,sqluser,sqlpass,sqldb, charset='utf8',port=port1)
    cursor1 = db.cursor()
    sql = "INSERT INTO chat (user,neirong,zt,shijian,towho) VALUES ('%s','%s','%s','%s','%s')"
    data1= (user1,message1,1,nowtime,towho1)
    ##print(data1,sql)
    cursor1.execute(sql % data1)
    db.commit()  ##数据更新后一定要这句
    db.close()
    return

def txtread(filename1):
    import _locale  ##中文不能正常显示的问题
    _locale._getdefaultlocale = (lambda *args: ['zh_CN', 'utf8']) ##中文不能正常显示的问题
    ##books.txt 是这样写入的  康熙 电子书 书柜    中间是空格
    fo1=open(filename1,"r")  ##打开文件
    lines=fo1.readlines()  ##把所有内容读入到lines变量内
    fo1.close() ##关闭文件
    #print(lines[0])  ##第一行  #print(lines[1])  ##第二行
    alldata=[]   ##初始化list, 后续要把所有的内容切片,放入alldata 列表内 1行就有3个变量,2行就是6个变量,最后一个是 alldata[5]
    for i in range(len(lines)):
        for j in range(3):
            temp=lines[i].split( ) ##行切片,.以空格来切,
            alldata.append(temp[j])
    return alldata
