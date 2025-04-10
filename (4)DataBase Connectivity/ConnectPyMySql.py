import pymysql
con = pymysql.connect(host='localhost',user='root',password='',database='test_db')
if(not con==None):
    print('Connection Successful!')
#closing the connection
    con.close()
