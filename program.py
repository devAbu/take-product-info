import pandas as pd

def takeName(name):
    data=pd.read_csv("skladiste.txt").to_records()
    
    for p in data: 
        if p.Naziv == name: 
            print(p.cijena)
            print(p.skladiste)

where = input("Unesi product: ")
takeName(where)