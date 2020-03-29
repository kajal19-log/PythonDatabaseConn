import mysql.connector#for connector
from mysql.connector import errorcode#for error handling
import pandas 


try:
  dbb = mysql.connector.connect(user='root', password='root',
                            host='127.0.0.1',database='db')
  print(dbb)#step to check what goes in 
  cursor = dbb.cursor()#reference to database
  '''
  m=input("Enter seat no: ")
  n=input("Enter name: ")
  query= "select * from students where seatno='%s'or name='%s'"%(m,n)
  '''
  query= "select * from customers"
  cursor.execute(query)#query to run
  res = cursor.fetchall()#get the result
  print(res)
  results = pandas.read_sql_query(query, dbb)
  results.to_csv("output.csv", index=False)
  if cursor.rowcount<1:
    print("No record found")
  else:  
        print("total records ",cursor.rowcount)
        for row in res:
          print("Customer Id:",row[0],"  Customer Name:",row[1],"City:",row[2]," Rating",row[3],"Salesperson id:",row[4])

except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Acess denied/wrong  user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exists")
  else:
    print(err)
else:
  dbb.close()



#m=input("Enter name to id: ") 
  #query= "select * from patient where PatientId='%s'"%m

