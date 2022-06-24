import psycopg2

try:

    connection = psycopg2.connect(
        user="postgres",
        password="postgres",
        host="172.17.",
        port="5432",
        database="postgres",
    )
    cursor = connection.cursor()
    insert_data = """insert into public.employee_data (e_id, e_name,salary,dob) values (2,'akash',30000,
    '1999-11-22')"""
    cursor.execute(insert_data)
    connection.commit()
    print("employee data inserted")
    cursor.execute("select * from employee_data")
    print("the inserted data are :", cursor.fetchall())

    # for update query
    update_query = "update employee_data set e_name='rajesh' where e_id=2;"
    cursor.execute(update_query)
    connection.commit()
    print("e_name is updated")
    cursor.execute("select * from employee_data")
    print("the inserted data are :", cursor.fetchall())

    # for deleted query
    deleted_query = "delete from employee_data  where e_id=2;"
    cursor.execute(deleted_query)
    connection.commit()
    print("data is deleted")
    cursor.execute("select * from employee_data")
    print("the inserted data are :", cursor.fetchall())

except (Exception, psycopg2.Error) as Error:
    print("error while inserted")
finally:
    if connection:
        cursor.close()
        connection.close()
        print("connection is closed")
