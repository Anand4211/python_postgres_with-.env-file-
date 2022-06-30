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

    cursor.execute('''select * from color where id between 2 and 5 order by color_name;''')
    logging.info(cursor.fetchall())

    cursor.execute('''select * from color where color_name in ('pink','sink') order by color_name;
                   ''')
    logging.info(cursor.fetchall())

    cursor.execute('''select * from color where color_name  not in ('pink','sink') order by color_name;
                       ''')
    logging.info(cursor.fetchall())


except(Exception, psycopg2.Error) as e:
    print(e)
