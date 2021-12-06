def connectMySQL(val):
    import mysql.connector as m
    try:
        #global mydb
        mydb = m.connect(
            host = "localhost",
            user = "root",
            password = "root",
            port = 3306,
            auth_plugin = 'mysql_native_password'
        )

        #global mycursor
        mycursor = mydb.cursor()
    except:
#        raise Exception("Please Launch MySQL")
        val = False
    finally:
        return val

