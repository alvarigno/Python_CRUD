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
name = "Book - A"
price = 125
    
insert_records = '''INSERT INTO Books(Name, Price) VALUES(?,?) ''' 
cursor.execute(insert_records, name, price)
cnxn.commit()