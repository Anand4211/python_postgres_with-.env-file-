import psycopg2
import logging
from config import config

from psycopg2.extras import LoggingConnection

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("logger information")


def connect():
    """ Connect to the PostgreSQL database server """

    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        connection = psycopg2.connect(connection_factory=LoggingConnection, **params)
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
        logging.info("Error in create operation", error)

    finally:
        # closing database connection.
        connection.close()
        logging.info('connection is closed')


if __name__ == "__main__":
    connect()
