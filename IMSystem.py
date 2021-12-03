import csv
import mysql.connector as m
import string

try:
    print("Connecting to MySQL...")
    mydb = m.connect(
        host="localhost",
        user="root", 
        password="root",
        port = 3306,
        auth_plugin='mysql_native_password'
    )
    print("Connection has been established")
except:
    print("Please Launch MySQL first!")
    exit()
else:
    print("Connection established")

mycursor = mydb.cursor()

##Creating the database structure
try:
    mycursor.execute("CREATE DATABASE inventorySystem")
except:
    pass

mycursor.execute("USE inventorySystem")

try:
    mycursor.execute("CREATE TABLE item (item_id INT AUTO_INCREMENT PRIMARY KEY, item_name VARCHAR(20), item_type ENUM('monitor','cpu','gpu','storage','case'))")
    mycursor.execute("CREATE TABLE orders (item_name VARCHAR(20), item_type ENUM('monitor','cpu','gpu','storage','case'), order_status VARCHAR(10))")
    mydb.commit()
    mycursor.execute("ALTER TABLE item AUTO_INCREMENT = 1000")
    mydb.commit()
except:
    pass
##Adding inventory to the database
mycursor.execute("INSERT INTO item(item_name, item_type) values ('Intel Core i5','cpu')")
mycursor.execute("INSERT INTO item(item_name, item_type) values ('Intel Core i7','cpu')")
mycursor.execute("INSERT INTO item(item_name, item_type) values ('Samsung 2TB SSD','storage')")
mycursor.execute("INSERT INTO item(item_name, item_type) values ('Sandisk 1TB SSD','storage')")
mycursor.execute("INSERT INTO item(item_name, item_type) values ('LG Ultrawide HDR','monitor')")
mycursor.execute("INSERT INTO item(item_name, item_type) values ('Samsung IPS 4K','monitor')")
mycursor.execute("INSERT INTO item(item_name, item_type) values ('Corsair Airflow','case')")
mycursor.execute("INSERT INTO item(item_name, item_type) values ('MSI AMD Radeon','gpu')")

mycursor.execute("INSERT INTO orders values ('Intel Core i7','cpu','pending')")
mycursor.execute("INSERT INTO orders values ('Samsung IPS 4K','monitor','shipped')")
mycursor.execute("INSERT INTO orders values ('Samsung 4TB HDD','storage','pending')")
mycursor.execute("INSERT INTO orders values ('Intel Core i3','cpu','shipped')")


mydb.commit()

choice = 0

while choice != '':
##Displays the Menu
    print("1. Import Item")
    print("2. View Inventory")
    print("3. Export Item")
    print("4. Place Order")
    print("5. View Orders")
    print("6. Exit")

    choice = int(input())

    print("[",choice,"]")

    if choice == 1:
        print("\nIMPORT ITEM")
        typeCheck = False
        while typeCheck == False:
            nameNewItem = input("enter [item name] to continue \nEnter [0] to return to main menu: ")
            if nameNewItem == '0':
                break
            typeNewItem = input("enter the item type \n[monitor, cpu , gpu, storage, case]: ")
            countNewItem = input("enter the number of items: ")
            try:
                for x in range(int(countNewItem)):
                    query1 = """INSERT INTO item(item_name, item_type) VALUES (%s, %s)""" 
                    val = (nameNewItem, typeNewItem)
                    mycursor.execute(query1, val) 
                mydb.commit()
            except:
                print("ITEM(S) DO NOT HAVE APPROPRIATE TYPE")
            else:
                typeCheck = True
                print("Item(s) have been imported")

    if choice == 2: #now is "track item"
        print("\nVIEW INVENTORY")
        query2 = """SELECT * FROM item""" 
        mycursor.execute(query2) 
        myresult = mycursor.fetchall() 
 
        ##Prints the results 
        for row in myresult: 
            print('{:>15}  {:>15}  {:>15}'.format(*row))
        ##If nothing is returned, the inventory is empty
        if mycursor.rowcount == 0:
            print("The inventory is empty!\n")

##        idCheck == False
##        while idCheck == False:
##            itemId = input("enter ")

    if choice == 3: # exporting an item
        exitCheck = False
        while exitCheck == False:
            exportID = input("\nenter 4 digit item ID to export \nor [0] to return to main menu: ") 
            if exportID == '0':
              break
            queryCheck = """SELECT * FROM item WHERE item_id = %s"""
            val = (int(exportID), )
            mycursor.execute(queryCheck, val)
            myresult = mycursor.fetchall()

            if mycursor.rowcount == 0:
                print("the item ID you have entered does not exist")
            else:
                query3 = """DELETE FROM item WHERE item_id = %s"""
                val = (int(exportID), )
                mycursor.execute(query3, val)
                mydb.commit()
                print("item "+ exportID +" has been exported")

    if choice == 4: ## placing orders
        print("\nPLACE ORDER")
        exitCheck = False
        while exitCheck == False:
            nameOrder = input("\nenter the item name\nor enter [0] to return to main menu: ")
            statusOrder = 'pending'
            if nameOrder == '0':
                break
            typeOrder = input("enter the item type\n[monitor, cpu , gpu, storage, case]: ")
            orderCount = input("enter the number of orders: ")

            try:
                for x in range(int(orderCount)):
                    query4 = """INSERT INTO orders(item_name, item_type, order_status) VALUES (%s, %s, %s)"""
                    val = (nameOrder, typeOrder, statusOrder)
                    mycursor.execute(query4, val)
                mydb.commit()
            except:
                print("ITEM(S) DO NOT HAVE APPROPRIATE TYPE")
            else:
                exitCheck = True
                print("your order(s) have been submitted")

    if choice == 5: #view orders
        query5 = """SELECT * FROM orders"""
        mycursor.execute(query5)
        myresult = mycursor.fetchall()

        ##Prints the results
        for row in myresult:
            print('{:>15}  {:>15}  {:>15}'.format(*row))
        ##If nothing is returned, the inventory is empty
        if mycursor.rowcount == 0:
            print("There are no existing orders\n")

    if choice == 6:
        ##deletes the database then closes this program
        print("Logging Out")
        exit()
    else:
        print("\n-- MAIN MENU --")
#mycursor.execute("DROP DATABASE inventorySystem")
