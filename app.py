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

if __name__=='__main__':
     app.run('0.0.0.0','5000')

output_file_name="./doc/output.csv"
input_file_name="./doc/nesting_example.csv"

def read():
    with open(output_file_name, 'w', newline='') as fOut:
        writer = csv.writer(fOut)
        with open(input_file_name, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                sum=0
                count=0
                for score in row[1:]:
                    sum+=int(score)
                    count+=1
                writer.writerow([row[0],str(sum/count)])

