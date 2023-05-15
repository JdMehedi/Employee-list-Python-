import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="pcrud",
    auth_plugin='mysql_native_password'
)

# return more than one row of data from the database server:
c = db.cursor()

c.execute("CREATE DATABASE pcrud")

# created employee table
emTable = """CREATE TABLE `pcrud`.`employee` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `department` VARCHAR(45) NULL,
  `salary` INT NULL,
   PRIMARY KEY (`id`))"""

c.execute(emTable)

# this statement will enable us to insert multiple rows at once.
empInsert = """INSERT INTO employee (
   name, department, salary)
   VALUES  (%s, %s, %s)"""

data = [("Vani", "HR", "100000"),
        ("Krish", "Accounts", "60000"),
        ("Aishwarya", "Sales", "25000"),
        ("Govind", "Marketing", "40000")]

c.executemany(empInsert, data)
db.commit()

# Retrieve all data
retriveData = """SELECT * FROM employee"""
c.execute(retriveData)
employee_data = c.fetchall()
for x in employee_data:
    print("All employee data is shown here: ", x)


# Update data
updateData = """update employee
set name = "mehedisdffg" where id = 2 """
c.execute(updateData)
db.commit()

# delete a specific data
empDelete = "DELETE FROM employee WHERE id=8"
c.execute(empDelete)
db.commit()
db.close()
