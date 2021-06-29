from flask import Flask
import csv
from configparser import ConfigParser
import psycopg2
from psycopg2 import Error
import csv
from types import new_class
output_file_name="./from_csv/output.csv"
input_file_name="./from_csv/nesting_example1.csv"

app = Flask(__name__)

@app.route("/")
def main_page():
    ''' this is the main page of the size
    '''
    return "<p>Hello, World!david </p>"

@app.route("/addNewNesting")
def add_new_nesting():
    ''' for add a new nesting wiht CVS file
    '''
    return "<p>add a new nestjing </p>"

@app.route("/getInventory")
def get_inventory():
    ''' get inventory from partial plates
    '''
    return "<p>connect to database to get inventory  list </p>"

############### classes 
class Steel(): 
    """ Steel class for size of steel 
    """
    def __init__(self,length,width,thickness,material) -> None:
        self.length=length
        self.width=width
        self.thickness=thickness
        self.material=material
        pass

    def get_steel(self)->list:

        return [self.length,self.width,self.thickness,self.material]
class Part(): 
    """ Part class 
    """
    def __init__(self,name) -> None:
        self.name=name
        pass

class Nesting(): 
    """ Nesting class 
    """
    def __init__(self,name) -> None:
        self.name=name
        pass

def read_from_csv()->dict:
    nesting=dict()
    with open(input_file_name, newline='') as f:
        reader = csv.reader(f)
        for i in reader:
            nesting[i[0]]=i[1:]
        return nesting

# see the link below about database.ini
# https://www.postgresqltutorial.com/postgresql-python/connect/
def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return db

def insert_nesting(nesting):
    sql_list=list()
    # sql s100
    sql="INSERT INTO makeoruse(use) VALUES (true) ;"
    sql_list.append(sql)

    nesting_name=nesting["nesting_name"][0]
    sql="INSERT INTO nesting(name,makeoruse_id) VALUES ('{}',{});".format(nesting_name,\
        "(SELECT makeoruse_id from makeoruse WHERE use=true ORDER BY public.makeoruse.makeoruse_id DESC LIMIT 1)")
    sql_list.append(sql)

    steel_used=Steel(nesting["length"][0],nesting['width'][0],thickness=nesting["thickness"][0],\
        material=nesting["material"][0])
    # for updating if the partial plate is exist
    check_steel_exist(steel_used)
    # insert the steel with makeoruse_id same as last one that made in "sql s100" 
    sql="INSERT INTO steel(length,width,thickness,material,makeoruse_id)VALUES({},{},{},\'{}\',{});\
            ".format(steel_used.length,steel_used.width, steel_used.thickness,steel_used.material,\
                '(SELECT makeoruse_id from makeoruse WHERE use=true ORDER BY public.makeoruse.makeoruse_id DESC LIMIT 1)')
    sql_list.append(sql)

    if nesting["rest_size"]: # some nesting does not have rest material
        steel_rest = Steel(nesting["rest_size"][0], nesting["rest_size"][1], thickness=nesting["thickness"][0],\
            material=nesting["material"][0])
        # it make a row in makeoruse tabele for the partial palte
        sql="INSERT INTO makeoruse(make,use) VALUES (true,false) ;"
        sql_list.append(sql)
        # isnert the steel in steel tabel 
        sql="INSERT INTO steel(length,width,thickness,material,makeoruse_id)VALUES({},{},{},\'{}\',{});\
            ".format(steel_rest.length,steel_rest.width, steel_rest.thickness,steel_rest.material,\
                '(SELECT makeoruse_id from makeoruse WHERE make=true ORDER BY public.makeoruse.makeoruse_id DESC LIMIT 1)')
        sql_list.append(sql)

    parts=list()
    for a in nesting["part"]:
        if a:
            part=Part(a)
            parts.append(part)
    for part in parts:
        sql='INSERT INTO part(name,nesting_id) VALUES (\'{}\',{});'.format(part.name,"(SELECT public.nesting.nesting_id from nesting WHERE name=\'{}\' ORDER BY public.nesting.nesting_id DESC LIMIT 1)".format(nesting_name))
        sql_list.append(sql)
    try:
        # Connect to an existing database
        params = config()
        connection = psycopg2.connect(**params)
        # Create a cursor to perform database operations
        cursor = connection.cursor()
        for sql in sql_list:
            print(sql)
            cursor.execute(sql)

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def steel_inventory():
    sql= "SELECT length,width,material FROM makeoruse INNER JOIN steel ON steel.makeoruse_id = makeoruse.makeoruse_id\
            WHERE  make=false;"

    try:
        # Connect to an existing database
        params = config()
        connection = psycopg2.connect(**params)

        # Create a cursor to perform database operations
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        
        # # Fetch result
        record = cursor.fetchone()
        while not record == None:
            print(record)
            record = cursor.fetchone()

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def check_steel_exist(steel_used):
    """ checks, if the steel has used for nesting, is available, if it is, it will update the use column of the row 
    and it will return true """

    sql='SELECT makeoruse_id FROM steel \
        WHERE  length={} and width={} and thickness={} and material=\'{}\' AND makeoruse_id={} LIMIT 1' \
        .format(steel_used.length,steel_used.width, steel_used.thickness,steel_used.material,\
        '(SELECT makeoruse_id FROM makeoruse WHERE use=false)'
            )

    result_for_return=None
    
    try:
        # Connect to an existing database
        params = config()
        connection = psycopg2.connect(**params)

        # Create a cursor to perform database operations
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        
        # # Fetch result
        record = cursor.fetchone()
        print(type(record))
        if record:
            #print(record)
            sql='UPDATE makeoruse SET use=true WHERE makeoruse_id={}'.format(record[0])
            cursor.execute(sql)
            connection.commit()
            result_for_return=True
        else:
            result_for_return=False 

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
            return result_for_return



#nesting=read_from_csv()
#insert_nesting(nesting)
#a=Steel(300,400,70,'steel1')
#print (check_steel_exist(a))
#steel_inventory()
#print (nesting)


# if __name__=='__main__':
#      app.run('0.0.0.0','5000')
