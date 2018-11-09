import pandas as pd

#create function called takeName with one parameter - name
def takeName(name):
    # read the txt file which includes products data
    # make each line a record array
    data=pd.read_csv("skladiste.txt").to_records()
    
    # go through each record array
    for p in data:
        # check if entered product's name exists
        if p.Naziv == name: 
            #print product's information
            print("CIJENA: {}  SKLADISTE: {}".format(p.cijena, p.skladiste))
# user input
where = input("Unesi product: ")
# call created function
takeName(where)