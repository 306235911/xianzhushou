# -*- coding:utf-8 -*-

import MySQLdb

class Mysql:
    
    # 连接数据库
    def __init__(self):
        try:
            # 连接中加上的 charset="utf8" 可省略下面的 self.db.set_character_set('utf8')
            self.db = MySQLdb.Connect('localhost' , 'root' , '306235911' , 'xian', charset="utf8")
            self.cur = self.db.cursor()
        except MySQldb.Error , e:
            print "连接数据库错误，原因 %d : %s" % (e.args[0] ,e.args[1])
            
    def insertData(self, identity , name, detal, img1 , img2 , img3 , title):
        # sql = "INSERT INTO book VALUES (%d,%s,%s,%s,%s)" % (identity , name , info , score , num)
        sql = "INSERT INTO item VALUES " + "(%s,%s,%s,%s,%s,%s,%s)"
        try:
            self.db.set_character_set('utf8')
            # result = self.cur.execute(sql)
            
            # 比起 "INSERT INTO table VALUES(%s,%s,%s)" % (a,b,c) 的用法，更常用的为下面的表达
            result = self.cur.execute(sql,(identity , name , detal , img1 , img2 , img3 , title))
            # insert_id = self.db.insert_id()
            self.db.commit()
            if result:
                return True
            else:
                return False
        except MySQLdb.Error , e:
            self.db.rollback()
            if "'key'PRIMARY" in e.args[1]:
                print u"数据已存在，未插入数据"
            else:
                print "插入数据失败，原因 %d : %s" % (e.args[0] ,e.args[1])
    
    # 创建数据库表            
    def createTable(self):
        sql = """CREATE TABLE book (
        identity INT(10) UNSIGNED NOT NULL PRIMARY KEY,
        name CHAR(60) NOT NULL,
        info CHAR(90) NOT NULL,
        score CHAR(10) NOT NULL,
        num CHAR(20) NOT NULL,
        bookType CHAR(40) NOT NULL,
        bookUrl CHAR(60) NOT NULL,
        imgUrl CHAR(60) NOT NULL);""" 
        # drop = "DROP TABLE IF EXISTS %s" % table
 
        try:
            # self.cur.execute(drop)
            self.cur.execute(sql)
            print u"创建数据库表成功"
        except MySQLdb.Error,e:
            self.db.rollback()
            print u"创建数据库表失败,原因" + " %d : %s" % (e.args[0] , e.args[1])
        except:
            print u"数据库语言错误"
            
            
    def main(self):
        identity = raw_input('identity\n')
        name = raw_input('name\n')
        detal = raw_input('detal\n')
        img1 = raw_input('img1\n')
        img2 = raw_input('img2\n')
        img3 = raw_input('img3\n')
        title = raw_input('title\n')
        
        self.insertData(identity , name , detal , img1 , img2 , img3 , title)
        
hah = Mysql()
hah.main()