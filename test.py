
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
            # >>> print(nesting_name)
            #['P202120', '', '', '', '']
            steel_used=Steel(nesting["length"][0],nesting['width'][0],tickness=nesting["thickness"][0],\
                material=nesting["material"][0])
            steel_rest = Steel(nesting["rest_size"][0], nesting["rest_size"][1], tickness=nesting["thickness"][0],\
                material=nesting["material"][0])
            writer.writerow(steel_used.get_steel())
            writer.writerow(steel_rest.get_steel()) 


read()





