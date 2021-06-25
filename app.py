from flask import Flask
import csv


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

# if __name__=='__main__':
#      app.run('0.0.0.0','5000')



import csv
from types import new_class
output_file_name="./doc/output.csv"
input_file_name="./doc/nesting_example.csv"


class Steel(): 
    """ Steel class for size of steel 
    """
    def __init__(self,length,width,tickness,material) -> None:
        self.length=length
        self.width=width
        self.tickness=tickness
        self.material=material
        
        pass
    def get_steel(self)->list:

        return [self.length,self.width,self.tickness,self.material]
    

class Part(): 
    """ Part class 
    """
    def __init__(self,name) -> None:
        self.name
        pass

def read():
    nesting=dict()
    with open(output_file_name, 'w', newline='') as fOut:
        writer = csv.writer(fOut)
        with open(input_file_name, newline='') as f:
            reader = csv.reader(f)
            for i in reader:
                nesting[i[0]]=i[1:]
            nesting_name=nesting["nesting_name"]
            # '''>>> print(nesting_name)
            # ['P202120', '', '', '', '']'''
            steel_used=Steel(nesting["length"][0],nesting['width'][0],tickness=nesting["thickness"][0],\
                material=nesting["material"][0])
            steel_rest = Steel(nesting["rest_size"][0], nesting["rest_size"][1], tickness=nesting["thickness"][0],\
                material=nesting["material"][0])
            writer.writerow(steel_used.get_steel())
            writer.writerow(steel_rest.get_steel()) 


#read()





import psycopg2

conn = psycopg2.connect(database="postgres", user = "postgres", password = "pass", host = "127.0.0.1", port = "5432")

print ("Opened database successfully")