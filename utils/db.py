from peewee import SqliteDatabase

def getDBConnection():
    try:
        print("Connecting to DB")
        dbConn=SqliteDatabase("db.sqlite")
        dbConn.connect()
        print("Connected")
        return dbConn
    except Exception as e:
        print(e) 
    
        
    


