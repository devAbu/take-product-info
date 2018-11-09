Products information
--------------------
--------------------

	- Products information solve problem of long-search through the file. With this projects users will easily just    write the product's name and get its information.

Features
--------

	- Make searching faster

How it's working
----------------

	- Read data from file and store the data as record array
		
		*** data=pd.read_csv("skladiste.txt").to_records() ***
	
	- Check if entered product name exists in the file and print its info
		
		*** 
			if p.Naziv == name: 
				print("CIJENA: {}  SKLADISTE: {}".format(p.cijena, p.skladiste)) ***
			
More details
------------

	- Function:
		
		takeName(var) --> used to check if entered product name exists in the file, if yes to write its informations

	- Variables: 
		
		-- data --> read the text file where the data is stored
		-- p --> go through data and split each data into lines
		-- where --> user input
			
Contribute
----------

	- Source code: github.com/devAbu/take-product-info