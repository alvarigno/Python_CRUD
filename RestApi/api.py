import pyodbc
server = 'tcp:localhost'
database = 'LibraryDB'
username = 'sa'
password = 'jobver@22'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT @@version;")
row = cursor.fetchone()
while row:
    print (row)
    row = cursor.fetchone()

#Inser data into SQL Server by Pythonb 
record_1= ["Book - B", 300]
record_2= ["Book - C", 200]
    
record_list = []
record_list.append(record_1)
record_list.append(record_2)
    
insert_records = '''INSERT INTO Books(Name, Price) VALUES(?,?) ''' 
cursor.executemany(insert_records, record_list)
cnxn.commit()

# select records
select_record = '''SELECT * FROM Books'''
cursor.execute(select_record)
     
for row in cursor:
    print(row)