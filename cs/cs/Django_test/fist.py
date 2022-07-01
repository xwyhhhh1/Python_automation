# -*- coding: utf-8 -*-
import xlwt
import os
list=("序号","mem","swap","磁盘使用率","cpu空闲率","备注")
#os.system方法只会返回一些0或者1的返回值，可参考shell中的$?想要获取命令执行结果需要用到管道方法os.popen方法获取执行结果集，read读取结果
#命令执行变量
mem=os.popen("free -h |awk 'NR==2{print $4}'")
swap=os.popen("free -h |awk 'NR==3{print $4}'")
Disk_mem=os.system("df -Th | awk '{print $6}' | grep -Evi 'use' >> /tmp/check_data_daily.txt")
Disk_mem_height=os.popen("df -Th | awk '{print $6}' | grep -Evi 'use' | wc -l")
Cpu_free=os.popen("iostat -c | awk 'NR==4{print $6}'")
k=1
#路径变量
path1='C:/Users/Administrator/Desktop/项目文档/和府捞面/test.xlsx'
path2="/root/tmp/test.xlsx"
path3="/tmp/check_data_daily.txt"


#创建一个excel表对象
xlsx=xlwt.Workbook(encoding='utf-8')
sheet1=xlsx.add_sheet('日常巡检数据',cell_overwrite_ok=True)

#表格样式
def fist():
    style=xlwt.XFStyle()# 创建样例对象
    alinment=xlwt.Alignment()# 创建排版类样例方法对象
    font=xlwt.Font()# 创建字体类样例对象
    pattern=xlwt.Pattern()# 创建背景颜色类对象
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour=70
    font.bold=True
    font.height=20*11
    alinment.horz=alinment.HORZ_CENTER# 水平居中对齐
    alinment.vert=alinment.VERT_CENTER# 垂直居中对齐
    style.alignment=alinment# 样例赋给样例对象
    style.font=font
    style.pattern=pattern
    return style

def second():
    style=xlwt.XFStyle()
    alignment=xlwt.Alignment()
    alignment.horz=alignment.HORZ_CENTER
    alignment.vert=alignment.VERT_CENTER
    font=xlwt.Font()
    font.height=20*11
    style.alignment=alignment
    style.font=font
    return style
sheet1.write_merge(0,0,0,5) # 设置第0行到第0行，第0列到第6列合并单元格
sheet1.col(0).width = 256 * 15  # Set the column width 设置第一列列宽
sheet1.col(1).width = 256 * 15  # Set the column width 设置第二列列宽
sheet1.col(3).width = 256 * 15  # Set the column width 设置第三列列宽
sheet1.col(4).width = 256 * 15  # Set the column width 设置第四列列宽
sheet1.col(5).width = 256 * 15  # Set the column width 设置第五列列宽


#一重循环写入表格基本结构
#二重循环写入序号
a=int(Disk_mem_height.read())
for i in range(0,6):
    sheet1.write(1,i,list[i],second())
    for j in range(1,a+1):
        sheet1.write(j+1,0,j,second())
DataFile=open(path3,'r')
for x in DataFile.readlines():
   k=k+1
   sheet1.write(k,3,x,second())
DataFile.close()
#写入两条命令的执行结果集
sheet1.write(0,0,"和府服务器日常巡检",fist())
sheet1.write(2,1,mem.read(),second())
sheet1.write(2,2,swap.read(),second())
sheet1.write(2,4,Cpu_free.read(),second())
#xlsx.save('C:/Users/Administrator/Desktop/项目文档/和府捞面/test.xlsx')
#正式生成excel表格文件
xlsx.save(path2)



