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
    create_t = """ drop table if exists employee_data """
    cursor.execute(create_t)
    connection.commit()

    create_table1 = """create table  employee_data (e_id int, e_name varchar(20)  ,salary int ,
    dob date); """
    cursor.execute(create_table1)
    connection.commit()
    print("Table created")
    cursor.execute("""select e_id from employee_data;""")
    logging.info(cursor.fetchall())


except (Exception, psycopg2.Error) as error:
    print("Error in create operation", error)

finally:
    # closing database connection.
    connection.close()
    logging.info('connection is closed')
