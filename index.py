import logging
import psycopg2
from psycopg2.extras import LoggingConnection

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("logger information")

try:

    connection = psycopg2.connect(
        connection_factory=LoggingConnection,
        user="postgres",
        password="postgres",
        host="172.17.0.6",
        port="5432",
        database="postgres",
    )
    connection.initialize(logger)
    cursor = connection.cursor()

    create_t2 = """ drop table if exists employeew """
    cursor.execute(create_t2)
    connection.commit()

    create_table1 = """create table employeew(id int ,employee_name varchar(30),employee_address varchar(20))"""
    cursor.execute(create_table1)
    connection.commit()
    logging.info("employeew table created")

    insert_data = """insert into employeew(id, employee_name, employee_address) values (2,'akash', 'noida,up'),(3,
    'uday','mumbai,maharastra'),(4,'adam','london') """
    cursor.execute(insert_data)
    connection.commit()
    logging.info("employee1 data inserted")

    explain_quaries = """ explain select * from employeew where id=2"""
    cursor.execute(explain_quaries)
    logging.info(cursor.fetchall())

    create_index = """create index idx_inde on employeew(employee_name)"""
    cursor.execute(create_index)

    connection.commit()
    logging.info("index  created on employee_name")

    explain_quaries = """ explain select * from employeew where id=2"""
    cursor.execute(explain_quaries)
    print(cursor.fetchall())

    cursor.execute("""drop index idx_inde""")
    connection.commit()
    logging.info("index  deleted ")


except (Exception, psycopg2.Error) as error:
    print("Error in create operation", error)
