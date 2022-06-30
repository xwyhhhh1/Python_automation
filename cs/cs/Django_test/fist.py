# -*- coding: utf-8 -*-
import xlwt
import os
#创建一个excel表对象
xlsx=xlwt.Workbook(encoding='utf-8')
sheet1=xlsx.add_sheet('日常巡检数据',cell_overwrite_ok=True)
list=("序号","mem","swap","磁盘使用率","备注")
#os.system方法只会返回一些0或者1的返回值，可参考shell中的$?想要获取命令执行结果需要用到管道方法os.popen方法获取执行结果集，read读取结果
mem=os.popen("free -h |awk 'NR==2{print $4}'")
swap=os.popen("free -h |awk 'NR==3{print $4}'")
Disk_mem=os.system("df -Th | awk '{print $6}' | grep -Evi 'use' >> /tmp/check_data_daily.txt")
Disk_mem_height=os.popen("df -Th | awk '{print $6}' | grep -Evi 'use' | wc -l")
k=0
#路径变量
path1='C:/Users/Administrator/Desktop/项目文档/和府捞面/test.xlsx'
path2="/root/tmp/test.xlsx"
path3="/tmp/check_data_daily.txt"
sheet1.col(0).width = 256 * 20  # Set the column width 设置第一列列宽
sheet1.col(1).width = 256 * 20  # Set the column width 设置第二列列宽
sheet1.col(3).width = 256 * 20  # Set the column width 设置第三列列宽
sheet1.col(4).width = 256 * 20  # Set the column width 设置第四列列宽
sheet1.col(5).width = 256 * 20  # Set the column width 设置第五列列宽
#一重循环写入表格基本结构
#二重循环写入序号
a=int(Disk_mem_height.read())
for i in range(0,5):
    sheet1.write(0,i,list[i])
    for j in range(1,a+1):
        sheet1.write(j,0,j)
DataFile=open(path3,'r')
for x in DataFile.readlines():
   k=k+1
   sheet1.write(k,3,x)
DataFile.close()
#写入两条命令的执行结果集
sheet1.write(1,1,mem.read())
sheet1.write(1,2,swap.read())
#xlsx.save('C:/Users/Administrator/Desktop/项目文档/和府捞面/test.xlsx')
#正式生成excel表格文件
xlsx.save(path2)



