import psycopg2

try:

    db_connection = psycopg2.connect(
        user="postgres",
        password="postgres",
        host="172.17.",
        port="5432",
        database="postgres",
    )

    cursor = db_connection.cursor()
    create_t = """ drop table if exists employee_data """
    cursor.execute(create_t)
    db_connection.commit()

    create_table1 = """create table  employee_data (e_id int, e_name varchar(20)  ,salary int ,
    dob date); """
    cursor.execute(create_table1)
    db_connection.commit()
    print("Table created")
    cursor.execute("""select e_id from employee_data;""")
    print(cursor.fetchall())

except (Exception, psycopg2.Error) as error:
    print("Error in create operation", error)

finally:
    # closing database connection.
    if db_connection.is_connected():
        cursor.close()
        db_connection.close()

        print("PostgreSQL connection is closed")
