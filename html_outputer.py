#coding=utf8
__author__ = 'zyx'

import pymysql
import xlrd
from xlutils.copy import copy
import time


class HtmlOutputer(object):

    #写入EXCEL
    def output_excel(self,new_data,house_city):
        file=xlrd.open_workbook("soufang.xls")

        #获取已有sheet的行数
        nrow=file.sheets()[0].nrows
        if nrow!=0:
            nrow==nrow+1
        #复制原有sheet
        copy_file=copy(file)
        sheet=copy_file.get_sheet(0)
        #插入数据
        for row,item in enumerate(new_data):
            sheet.write((row+nrow),4,house_city)
            for i,value in enumerate(item.values()):
                sheet.write((row+nrow),i,value)
        copy_file.save('soufang.xls')


    #写入数据库
    def output_mysql(self,new_data,house_city):
        db=pymysql.connect(host="localhost",user="root",passwd="root",db="test",charset="utf8")
        cursor=db.cursor()
        try:
            for item in new_data:
                values=item.values()
                sql=("insert into SouFang (HouseAddr,HouseTag,HouseName,HousePrice,HouseCity,CrawDate) values('%s','%s','%s','%s','%s','%s')"
                     %(values[0].encode("utf8"),values[1].encode("utf8"),
                       values[2].encode("utf8"),values[3].encode("utf8"),
                       house_city.encode("utf8"),time.strftime('%Y-%m-%d',time.localtime(time.time())).encode("utf8"))
                     )
                cursor.execute(sql)
                db.commit()
        except:
            print(item["house_name"],"false")
            db.rollback()#发生错误时回滚
        db.close()