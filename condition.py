import logging
import psycopg2
from psycopg2.extras import LoggingConnection

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("loggerinformation")

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

    cursor.execute("""drop table if exists people""")
    connection.commit()

    create_table1 = """create table people(people_name varchar(30),people_age int)"""
    cursor.execute(create_table1)
    connection.commit()
    logging.info("people table created")

    insert_data = """insert into people( people_name, people_age) values ('deepaks',39),('rohit',45),('rahul',44) """
    cursor.execute(insert_data)
    connection.commit()
    logging.info("car data inserted")

    cursor.execute(
        """select people_name ,people_age from people  where people_name like '%_s' """
    )
    logging.info(cursor.fetchall())


except (Exception, psycopg2.Error) as error:
    print("Error in create operation", error)
