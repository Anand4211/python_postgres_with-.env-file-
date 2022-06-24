# python postgresql trigger
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

    create_t = """ drop table if exists client1 """
    cursor.execute(create_t)
    connection.commit()

    create_t2 = """ drop table if exists client2 """
    cursor.execute(create_t2)
    connection.commit()

    create_table1 = """create table client1 (id int primary key,client_name varchar(30),client_address varchar(20))"""
    cursor.execute(create_table1)
    connection.commit()
    print("client1 table created")

    create_table2 = """create table client2 (id int primary key,client_name varchar(30),client_address varchar(20),
    changed_on timestamp(5) not null) """
    cursor.execute(create_table2)
    connection.commit()
    print("client2 table created")

    # create function for triggers
    cursor.execute(
        """CREATE OR REPLACE FUNCTION log_backup_data()  
  RETURNS TRIGGER   
  LANGUAGE PLPGSQL  
  AS  
$$  
BEGIN  
    
    INSERT INTO client2(id,client_name,client_address,changed_on)  
         VALUES(OLD.id,OLD.client_name,OLD.client_address,now());  
     
RETURN OLD;  
END;  
$$  """
    )
    connection.commit()
    print("function created")

    # craete trigger and execute

    cursor.execute(
        """create trigger backup_data
                  after delete 
                  on client1
                  for  each row
                  execute procedure log_backup_data()"""
    )
    connection.commit()
    print(" triggers created")

    insert_data = """insert into client1(id, client_name, client_address) values (2,'akash', 'noida,up'),(3,
    'uday','mumbai,maharastra'),(4,'adam','london') """
    cursor.execute(insert_data)
    connection.commit()
    print("client1 data inserted")

    cursor.execute("select * from client1")
    print("the inserted data are :", cursor.fetchall())

    # deleted query
    deleted_query = "delete from client1  where id=3;"
    cursor.execute(deleted_query)
    connection.commit()
    print("client1_data is deleted")

    cursor.execute("select * from client2")
    print("the inserted data are :", cursor.fetchall())

except (Exception, psycopg2.Error) as Error:
    print("your query is not right")
