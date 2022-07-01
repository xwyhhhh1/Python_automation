import xlwt
import os
xlsx=xlwt.Workbook(encoding='utf-8')
sheet1=xlsx.add_sheet('日常巡检数据',cell_overwrite_ok=True)
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

sheet1.write_merge(0,0,0,3,'test')
sheet1.write(0, 0, "is test",style)
xlsx.save("C:/Users/Administrator/Desktop/项目文档/和府捞面/ceshi.xlsx")
