import pymysql

def mysqlconnect(): 
    conn = pymysql.connect( 
        host='localhost', 
        user='root',  
        db='test',
        ) 
      
    cur = conn.cursor() 
    cur.execute("select * from employees") 
    output = cur.fetchall() 
    apiobj = {}
    mainOutput = []
    for x in output :
        apiobj["name"] = x[1]
        apiobj["company"] = x[2]
        apiobj["skill"] = x[3]
        mainOutput.append(apiobj)
        apiobj = {}

    conn.close() 
    return mainOutput

mysqlconnect()