import mysql.connector as c
mydb = c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="teju"
)

if mydb.is_connected():
    print("Connection successful!")
else:
    print("Connection failed.")

mycursor = mydb.cursor()

while True:
    id = input("Enter player id (or type 'exit' to quit).... ")
    if id.lower() == 'exit':
        print("exiting the loop....")
        break

    name = input("Enter  name: ")
    department=input("enter the department")
    salary = input("Enter  salary: ")
    city = input("Enter city: ")
    

    mycursor.execute("insert into suppliers2(id, name, department,salary, city) VALUES (%s, %s, %s, %s, %s)", (id, name,department, salary, city))
    mydb.commit()
    print(f"supplier{name} with ID {id} inserted successfully.")

id_to_delete = input("Enter ID to delete: ")
mycursor.execute("delete from suppliers2 where id = %s", (id_to_delete,))
mydb.commit()
print(f"Player with ID {id_to_delete} deleted successfully.")

print("Update supplier details. Give  ID and details to update.")
id_to_update = input("Enter ID to update: ")
name_to_update = input("Enter name: ")
department_to_update=input("enter department:")
salary_to_update = input("Enter salary ")
city_to_update = input("Enter city: ")

mycursor.execute("update suppliers2 set name = %s, department=%s,salary = %s, city = %s where id = %s", (name_to_update,department_to_update, salary_to_update, city_to_update, id_to_update))
mydb.commit()
print(f"Supplier with ID {id_to_update} updated successfully.")

mycursor.execute("select * from suppliers2")
result = mycursor.fetchall()
print("\nAll Suppliers:")
for row in result:
    print(row)

mycursor.execute("select * from suppliers2 order by name ASC")
supplier_sorted = mycursor.fetchall()
print("\nSuppliers sorted by name:")
for p in supplier_sorted:
    print(p)

mycursor.execute("select * from suppliers2 where salary between 50000 AND 60000")
supplier_salary_range= mycursor.fetchall()
print("\nsuppliers with salary between 50000 and 60000:")
for a in supplier_salary_range:
    print(a)

mycursor.execute("select * from suppliers2 where city = 'Hyderabad'")
supplier_from_hyderabad = mycursor.fetchall()
print("\nsuppliers from Hyderabad:")
for b in supplier_from_hyderabad:
    print(b)
mydb.commit()
