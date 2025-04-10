import pymysql
con = pymysql.connect(host='localhost',user='root',password='',database='test_db')
if(not con==None):
    print('Connection Successful!')
cursor1 = con.cursor()
try:
    #executing the SQL Query
    
    cursor1.execute("INSERT INTO student(`name`,`rollno`,`age`,`marks`)VALUES('Tanmay',248074,17,80),('Kartik',248341,19,99);" )
    con.commit()
    print("Inserted data into the table")
    
    cursor1.execute("SELECT * FROM student; " )
    res=cursor1.fetchall()
    for record in res:
        print(record[0],record[1],record[2],record[3],)
    print("Retrived all data from table")

    cursor1.execute("UPDATE student SET age=20 WHERE rollno=248030 ;" )
    con.commit()
    print("Updated the row of the table")

    
    cursor1.execute("DELETE FROM student WHERE rollno = 24831;" )
    con.commit()
    print("Deleted the row of the table")
    
    cursor1.execute("CREATE TABLE employees (employee_id INT PRIMARY KEY,first_name VARCHAR(50),last_name VARCHAR(50),salary DECIMAL(10, 2));" )
    con.commit()
    print("Created a table")

except Exception as e:
    print("Exception Found!",e)
#closing the connection
con.close()
