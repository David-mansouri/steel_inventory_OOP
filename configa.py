import psycopg2
from psycopg2 import Error

try:
    # Connect to an existing database
    connection = psycopg2.connect(user="postgres",
                                  password="pass",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")

    # Create a cursor to perform database operations
    cursor = connection.cursor()
    # Print PostgreSQL details
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    # Executing a SQL query
    sql="INSERT INTO part(name) VALUES ('m');"
    #sql="SELECT * FROM public.part " 
    #sql='psql -U postgres -d postgre'
    # sql="""SELECT *
    # FROM pg_catalog.pg_tables
    # WHERE schemaname != 'pg_catalog' AND 
    #     schemaname != 'information_schema';"""



    
    cursor.execute(sql)
    connection.commit()

    # # Fetch result
    # record = cursor.fetchone()
    #print("You are connected to - ", record, "\n")


except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")