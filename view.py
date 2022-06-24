import psycopg2

try:
    connection = psycopg2.connect(user='postgres',
                                  password='postgres',
                                  port='5432',
                                  host='172.17.0.6',
                                  database='postgres')

    cursor = connection.cursor()

    create_t2 = """ drop table if exists employeew """
    cursor.execute(create_t2)
    connection.commit()
    create_t2 = """ drop table if exists salary """
    cursor.execute(create_t2)
    connection.commit()

    create_table1 = """create table employeew(id int primary key,employee_name varchar(30),employee_address varchar(20))"""
    cursor.execute(create_table1)
    connection.commit()
    print("employee1 table created")

    create_table2 = """create table salary (id int primary key,salary int,technology varchar(40)) """
    cursor.execute(create_table2)
    connection.commit()
    print("salary table created")

    insert_data = """insert into employeew(id, employee_name, employee_address) values (2,'akash', 'noida,up'),(3,
    'uday','mumbai,maharastra'),(4,'adam','london') """
    cursor.execute(insert_data)
    connection.commit()
    print("employee1 data inserted")
    insert_data = """insert into salary(id, salary,technology) values (2,100000,'dotnet'),(3,120000,'python'),(4,2000000,'python,java,sql') """
    cursor.execute(insert_data)
    connection.commit()
    print("employee data inserted")

    view_from_1_table = """CREATE VIEW View3 AS   
    SELECT employee_name   
    FROM employeew 
    WHERE id > '2';   """
    cursor.execute(view_from_1_table)
    connection.commit()
    cursor.execute("select * from view3")
    print("this is view from single table:", cursor.fetchall())

    view_from_2_table = """CREATE VIEW View AS   
    SELECT e.employee_name ,s.salary ,s.technology 
    FROM employeew as e
    join salary as s
    on e.id = s.id
    WHERE s.salary > '50000';   """
    cursor.execute(view_from_2_table)
    connection.commit()
    cursor.execute("select * from view ")
    print("this is view:", cursor.fetchall())

except (Exception, psycopg2.Error) as error:
    print("Error in create operation", error)
