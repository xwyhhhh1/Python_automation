import os
#public variable
MYSQL_URL = "https://mirrors.tuna.tsinghua.edu.cn/mysql/downloads/MySQL-5.7/mysql-5.7.38-linux-glibc2.12-x86_64.tar.gz"
DOWLOAD_MYSQL_CMD = "wget" + '\t' + MYSQL_URL + '\t' + "--no-check-certificate"
def install():
    de=os.system("netstat -a")
    dc=os.system(DOWLOAD_MYSQL_CMD)
    #ds=os.uname()
    return dc
if __name__ == '__main__':
    install()