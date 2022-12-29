import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=HCL-02-62\SQLEXPRESS;'
                      'Database=FileSearchResults;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute('''
    INSERT INTO FileSearchResults_tale(File_Location, SearchCount, NameofFile)
    VALUES
    ("E:\Folder_A\Folder_B\Folder_C\Empty_File.txt",1,'Empty_File.txt')
    ("E:\Folder_A\Folder_B\Folder_C\Folder_D\Folder_E\Folder_F\Empty_File.txt",3,'Empty_File.txt')
           ''')
conn.commit();
cursor.execute('Select * From FileSearchResults_table')
File_input = 'empty_file.txt'