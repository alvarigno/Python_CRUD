import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=localhost:1433'
                      'Database=LibraryDB;'
                      'Trusted_Connection=yes;'
                      'UID=sa;PWD=jobver@22;')

cursor = conn.cursor()
