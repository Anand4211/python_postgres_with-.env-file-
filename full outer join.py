import logging
import psycopg2
from psycopg2.extras import LoggingConnection

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("logger information")

try:

    connection = psycopg2.connect(connection_factory=LoggingConnection,
                                  user="postgres",
                                  password="postgres",
                                  host="172.17.0.6",
                                  port="5432",
                                  database="postgres",
                                  )
    connection.initialize(logger)
    cursor = connection.cursor()

    create_t2 = """ drop table if exists employee3"""
    cursor.execute(create_t2)
    connection.commit()
    create_t2 = """ drop table if exists salary1 """
    cursor.execute(create_t2)
    connection.commit()

    create_table1 = """create table employee3(id int primary key,employee_name varchar(30),
    employee_address varchar(20))"""
    cursor.execute(create_table1)
    connection.commit()
    logging.info("employee1 table created")

    create_table2 = """create table salary1 (id int primary key,salary int,technology varchar(100)) """
    cursor.execute(create_table2)
    connection.commit()
    logging.info("salary table created")

    insert_data = """insert into employee3(id, employee_name, employee_address) values (2,'akash', 'noida,up'),(3,
    'uday','mumbai,maharastra'),(4,'adam','london'),( 7,'rajesh','patna,bihar');"""
    cursor.execute(insert_data)
    connection.commit()
    logging.info("employee1 data inserted")

    insert_data = """insert into salary1(id, salary,technology) values (2,100000,'dotnet'),(3,120000,'python'),(4, 
    2000000,'python,java,sql'),(5,400000,'go,java,docker,sql,python,html,css,js'),
    (9,500000,'python,django,sql,html,css,docker,pandas') """
    cursor.execute(insert_data)
    connection.commit()
    logging.info("employee data inserted")

    full_joins = """select  employee3.employee_name,salary1.salary from employee3  full join salary1  on employee3.id 
    =salary1.id; """
    cursor.execute(full_joins)
    connection.commit()
    logging.info(cursor.fetchall())


except (Exception, psycopg2.Error) as Error:
    print("error while inserted")
